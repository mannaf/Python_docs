def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))


def concat(*args, sep="/"):
    return sep.join(args)


a = concat("mannaf", "love", "with sister")
b = concat("mannaf", "love", "with sister",sep=".")
print(a)
print(b)
