from abc import ABC, abstractmethod


class KakaoOauthService(ABC):
    @abstractmethod
    def kakaoLoginAddress(self):
        pass

    @abstractmethod
    def requestAccessToken(self, kakaoOauthCode):
        pass
