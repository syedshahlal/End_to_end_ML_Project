class VersionUpdater:
    def __init__(self, file_path='version.txt'):
        self.file_path = file_path
        self.current_version = self._read_version()

    def _read_version(self):
        try:
            with open(self.file_path, 'r') as file:
                return file.read().strip()
        except FileNotFoundError:
            return "0.0.0"

    def update_version(self):
        major, minor, patch = map(int, self.current_version.split('.'))
        patch += 1
        new_version = f"{major}.{minor}.{patch}"

        with open(self.file_path, 'w') as file:
            file.write(new_version)

        return new_version

if __name__ == "__main__":
    version_updater = VersionUpdater()
    new_version = version_updater.update_version()
