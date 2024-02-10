# get_next_video module
def get_next_video_link(file_path, current_link):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if current_link < len(lines):
                next_link = lines[current_link].strip()
                current_link += 1  # Update the current_link counter
                return next_link, current_link
            else:
                return None, current_link
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None, current_link
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, current_link