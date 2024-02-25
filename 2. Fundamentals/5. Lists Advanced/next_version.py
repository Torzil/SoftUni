def version_updater(ver):
    version[-1] += 1
    for index in range((len(version) - 1), 0, -1):
        if version[index] > 9:
            version[index] = 0
            version[index - 1] += 1
    return version


version = [int(ver) for ver in input().split(".")]
new_version = ".".join(map(str, version_updater(version)))
print(new_version)
