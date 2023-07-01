from yojna.models import SchemeRegistrationMediaModel


class SchemeRegistrationMediaService:

    def __init__(self):
        pass

    @staticmethod
    def handle_uploaded_in_memory_file(register_scheme, files):
        count=1
        for file in files:
            try:
                print('media')
                for media in files.getlist(file):
                    try:
                        if count == 1:
                            registration_media = SchemeRegistrationMediaModel(scheme_registration=register_scheme,
                                                                          category=file)
                            print('media2')
                            registration_media.arza = media
                            registration_media.save()
                            count+=1
                        else:
                            registration_media = SchemeRegistrationMediaModel(scheme_registration=register_scheme,
                                                                          category=file)
                            registration_media.file_path = media
                            registration_media.save()
                    except Exception as exc:
                        continue
            except Exception as exc:
                continue
