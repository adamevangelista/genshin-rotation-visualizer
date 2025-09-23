import json

# This mapping helps convert the short names in gcsim to the full names we want to display.
# This map must include all characters from all supported teams.
CHARACTER_NAME_MAP = {
    "xiao": "Xiao",
    "faruzan": "Faruzan",
    "xianyun": "Xianyun",
    "furina": "Furina",
    "bennett": "Bennett",
    "zhongli": "Zhongli",
    "albedo": "Albedo",
    "jean": "Jean",
    "mualani": "Mualani",
    "mavuika": "Mavuika",
    "xilonen": "Xilonen",
    "sucrose": "Sucrose",
    "citlali": "Citlali",
    "kazuha": "Kazuha",
    "xiangling": "Xiangling"
}

# This mapping helps standardize ability names for color-coding.
ABILITY_NAME_MAP = {
    "skill": "Skill",
    "burst": "Burst",
    "attack": "Normal Attack",
    "high_plunge": "Plunge"
}

def parse_gsim_file(filepath):
    """
    Reads a .gsim file, extracts the action list, and converts it into a structured
    list of dictionaries for the visualizer.
    """
    action_sequence = []
    
    try:
        with open(filepath, 'r') as f:
            for line in f:
                cleaned_line = line.strip()

                if not cleaned_line or cleaned_line.startswith('#'):
                    continue
                
                # Separate the main action from the full comment string
                action_part = cleaned_line.split('#')[0].strip().replace(';', '')
                comment_parts = cleaned_line.split('#')[1:]
                full_comment = "#".join(comment_parts)

                if not action_part:
                    continue

                parts = action_part.split()
                char_name_raw = parts[0]
                
                if char_name_raw not in CHARACTER_NAME_MAP:
                    continue

                # Get the primary action for color-coding (the first ability listed)
                primary_action = parts[1].split(':')[0]

                # Extract the tooltip label directly from the comment
                tooltip_label = "Action" # Default label
                if 'label=' in full_comment:
                    try:
                        tooltip_label = full_comment.split('label=')[1].split('#')[0].strip()
                    except IndexError:
                        pass # Keep default if label is malformed

                # Extract the duration for the entire line from the comment
                duration = 2.0 # Default duration
                if 'duration=' in full_comment:
                    try:
                        duration = float(full_comment.split('duration=')[1].split('#')[0].strip())
                    except (ValueError, IndexError):
                        pass
                
                action = {
                    "character": CHARACTER_NAME_MAP.get(char_name_raw, char_name_raw.title()),
                    "ability": ABILITY_NAME_MAP.get(primary_action, primary_action.title()),
                    "raw_ability": tooltip_label,
                    "duration": duration
                }
                action_sequence.append(action)

    except FileNotFoundError:
        print(f"Error: Could not find file at {filepath}")
        return []

    return action_sequence

if __name__ == '__main__':
    # This block allows for direct testing of the parser from the command line.
    # You can change the filename to test different team compositions.
    test_file = 'xiao_hypercarry.gsim'
    print(f"--- Testing parser with '{test_file}' ---")
    rotation = parse_gsim_file(test_file)
    print(json.dumps(rotation, indent=2))

