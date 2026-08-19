#!/usr/bin/env ruby
# Validates the portable SKILL.md convention documented by skills/create-skills.

require "yaml"

root = File.expand_path("..", __dir__)
skill_root = File.join(root, "skills")
errors = []
skill_files = Dir.glob(File.join(skill_root, "*", "SKILL.md")).sort

skill_files.each do |file|
  relative = file.sub("#{root}/", "")
  expected_name = File.basename(File.dirname(file))
  text = File.read(file)
  lines = text.lines

  unless lines.first&.strip == "---"
    errors << "#{relative}: frontmatter must begin on line 1 with ---"
    next
  end

  closing_line = lines[1..]&.index { |line| line.strip == "---" }
  unless closing_line
    errors << "#{relative}: frontmatter must end with ---"
    next
  end
  closing_line += 1

  begin
    metadata = YAML.load(lines[1...closing_line].join)
  rescue Psych::SyntaxError => error
    errors << "#{relative}: invalid YAML frontmatter (#{error.message.lines.first.strip})"
    next
  end

  unless metadata.is_a?(Hash)
    errors << "#{relative}: frontmatter must be a YAML map"
    next
  end

  unexpected = metadata.keys.map(&:to_s).sort - %w[description name]
  errors << "#{relative}: unsupported frontmatter key(s): #{unexpected.join(", ")}" unless unexpected.empty?
  errors << "#{relative}: name must equal directory name #{expected_name.inspect}" unless metadata["name"] == expected_name
  errors << "#{relative}: name must use lowercase letters, digits, and hyphens" unless expected_name =~ /\A[a-z0-9]+(?:-[a-z0-9]+)*\z/

  description = metadata["description"]
  errors << "#{relative}: description must be a non-empty string" unless description.is_a?(String) && !description.strip.empty?
  errors << "#{relative}: description must include a specific 'Use when' trigger" unless description.is_a?(String) && description.include?("Use when")

  body = lines[(closing_line + 1)..]&.join.to_s
  errors << "#{relative}: body must begin with a Markdown H1" unless body.match?(/\A\s*#\s+.+/)
  errors << "#{relative}: body exceeds 500 lines; move optional detail to a linked reference" if body.lines.length > 500
end

if errors.empty?
  puts "Skills convention: OK (#{skill_files.length} skills checked)"
  exit 0
end

warn "Skills convention errors:"
warn errors.map { |error| "- #{error}" }.join("\n")
exit 1
