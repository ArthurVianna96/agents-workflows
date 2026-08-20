#!/usr/bin/env ruby
# Answers whether this repository is coherent: every skill follows the portable
# SKILL.md convention documented by skills/create-skills, and every internal
# Markdown link resolves to something that exists.

require "yaml"

ROOT = File.expand_path("..", __dir__)

def relative(path)
  path.sub("#{ROOT}/", "")
end

errors = []

# --- Skill convention -------------------------------------------------------

skill_files = Dir.glob(File.join(ROOT, "skills", "*", "SKILL.md")).sort

skill_files.each do |file|
  name = relative(file)
  expected_name = File.basename(File.dirname(file))
  lines = File.read(file).lines

  unless lines.first&.strip == "---"
    errors << "#{name}: frontmatter must begin on line 1 with ---"
    next
  end

  closing_line = lines[1..]&.index { |line| line.strip == "---" }
  unless closing_line
    errors << "#{name}: frontmatter must end with ---"
    next
  end
  closing_line += 1

  begin
    metadata = YAML.load(lines[1...closing_line].join)
  rescue Psych::SyntaxError => error
    errors << "#{name}: invalid YAML frontmatter (#{error.message.lines.first.strip})"
    next
  end

  unless metadata.is_a?(Hash)
    errors << "#{name}: frontmatter must be a YAML map"
    next
  end

  unexpected = metadata.keys.map(&:to_s).sort - %w[description name]
  errors << "#{name}: unsupported frontmatter key(s): #{unexpected.join(", ")}" unless unexpected.empty?
  errors << "#{name}: name must equal directory name #{expected_name.inspect}" unless metadata["name"] == expected_name
  errors << "#{name}: name must use lowercase letters, digits, and hyphens" unless expected_name =~ /\A[a-z0-9]+(?:-[a-z0-9]+)*\z/

  description = metadata["description"]
  errors << "#{name}: description must be a non-empty string" unless description.is_a?(String) && !description.strip.empty?
  errors << "#{name}: description must include a specific 'Use when' trigger" unless description.is_a?(String) && description.include?("Use when")

  body = lines[(closing_line + 1)..]&.join.to_s
  errors << "#{name}: body must begin with a Markdown H1" unless body.match?(/\A\s*#\s+.+/)
  errors << "#{name}: body exceeds 500 lines; move optional detail to a linked reference" if body.lines.length > 500
end

# --- Internal links ---------------------------------------------------------

# [text](target), tolerating <angle brackets> and a "quoted title".
LINK = /\[[^\]]*\]\(\s*<?([^)>\s]+)>?(?:\s+"[^"]*")?\s*\)/
EXTERNAL = %r{\A(?:[a-z][a-z0-9+.-]*:|//)}i

tracked = IO.popen(%w[git -C] + [ROOT, "ls-files", "-z", "--", "*.md"]) { |io| io.read }
markdown_files = tracked.split("\0").reject(&:empty?).map { |path| File.join(ROOT, path) }.sort

# A silent failure here would report zero broken links because it checked none.
if !$?.success? || markdown_files.empty?
  errors << "scripts/validate.rb: found no tracked Markdown files to check (is this a git checkout?)"
end

links_checked = 0

markdown_files.each do |file|
  name = relative(file)
  fenced = false

  File.readlines(file).each_with_index do |line, index|
    # Illustrative links inside code fences point at example paths, not real ones.
    if line.start_with?("```", "~~~")
      fenced = !fenced
      next
    end
    next if fenced

    line.scan(LINK) do |(target)|
      next if target.start_with?("#")
      next if target.match?(EXTERNAL)

      path = target.split("#").first.to_s
      next if path.empty?

      links_checked += 1
      resolved = File.expand_path(path, File.dirname(file))
      next if File.exist?(resolved)

      errors << "#{name}:#{index + 1}: link does not resolve: #{target}"
    end
  end
end

# --- Report -----------------------------------------------------------------

if errors.empty?
  puts "Repository coherence: OK (#{skill_files.length} skills, #{links_checked} internal links)"
  exit 0
end

warn "Repository coherence errors:"
warn errors.map { |error| "- #{error}" }.join("\n")
exit 1
