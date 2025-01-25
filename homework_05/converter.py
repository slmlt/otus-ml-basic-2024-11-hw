from abc import ABC, abstractmethod

from media_file import MediaFile, MediaFormat


class MediaFileConverter(ABC):

    @abstractmethod
    def convert(self, file: MediaFile, target_format: MediaFormat) -> MediaFile:
        """
        Converts media file to given format and returns the result,
        or raises exception if conversion is not possible
        :param file: file to convert
        :param target_format: target format
        :raises ConversionError
        """
        pass

    @abstractmethod
    def is_convertible(self, file: MediaFile, target_format: MediaFormat) -> bool:
        """
        Checks if it is possible to convert media file to given format
        :param file: file to convert
        :param target_format: target format
        :returns True if file is convertible to target format, False otherwise
        """
        pass


class ConversionError(Exception):
    pass
