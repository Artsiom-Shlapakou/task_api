
def get_file_path(instance, filename):
    return "files/user_{0}/homework_{1}/{2}".format(instance.user, 
                                            instance.homework,
                                            filename)

