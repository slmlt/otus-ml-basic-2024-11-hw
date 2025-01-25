from abc import ABC, abstractmethod

from media_file import MediaFile


class MediaFileRepository(ABC):

    @abstractmethod
    def get_all(self) -> list[MediaFile]:
        """
        Reads all media file from storage
        :return list of media files
        """
        pass

    @abstractmethod
    def get(self, file_id: str) -> MediaFile:
        """
         Reads and returns media file from storage if it is present,
         or raises exception otherwise
         :param file_id: file id
         :raises FileNotFoundError error otherwise
        """
        pass

    @abstractmethod
    def save(self, file: MediaFile):
        """
        Saves media file to storage
        :param file: media file to save
        :raises IOError
        """
        pass

    @abstractmethod
    def remove(self, file_id: str):
        """
        Removes media file from storage
        :param file_id: file id
        :raises IOError
        """
        pass

    @abstractmethod
    def remove_all(self):
        """
        Removes all media files from storage
        :raises IOError
        """
        pass
