from collections.abc import Callable
import pytest
import hachicrypt.utils as utils
import hachicrypt.core as core

# from hachicrypt.core import encrypt, decrypt

def test_str_hash() :
    # pass
    hash1 = utils.stable_str_to_num("hachicrypt")  # 항상 같은 값
    hash2 = utils.stable_str_to_num("password123")
    print(hash1)
    print(hash2)
    #
    assert hash1 != hash2

def test_read_config() :
    ingredients = utils.read_from_section("botchi")
    print(ingredients)

def test_check_sections() :
    print("\nis good?")
    utils.check_section()

def test_encrypt_decrypt() :
    plaintext = "안녕 나는 하치야"
    encrypted = core.encrypt(plaintext, 5, "poorin")
    print("encrypted :: {}".format(encrypted))
    decrypted = core.decrypt(encrypted, 5, "poorin")
    print("decrypted :: {}".format(decrypted))

    assert plaintext != encrypted, "암호화된 문자열은 원본과 달라야 합니다. - 통과"
    assert encrypted != decrypted, "암호화와 복호화된 문자열이 달라야 합니다. - 통과"
    assert plaintext == decrypted, "원본과 복호화된 문자열이 같음 - 통과"

def test_encrypt() :
    plaintext = "안녕 나는 하치야"
    encrypted = core.encrypt(plaintext, 5, "pikachu")
    print("encrypted :: {}".format(encrypted))

def test_encrypt2() :
    _PLAIN_TEXT = """
    여름 장이란 애시당초에 글러서, 해는 아직 중천에 있건만 장판은 벌써 쓸쓸하고 더운 햇발이 벌여놓은 전 휘장 밑으로 등줄기를 훅훅 볶는다.마을 사람들은 거지반 돌아간 뒤요, 팔리지 못한 나뭇군패가 길거리에 궁싯거리고들 있으나 석윳병이나 받고 고깃마리나 사면 족할 이 축들을 바라고 언제까지든지 버티고 있을 법은 없다. 춥춥스럽게 날아드는 파리떼도 장난군 각다귀들도 귀치않다. 얽둑배기요 왼손잡이인 드팀전의 허생원은 기어코 동업의 조선달에게 낚아보았다.
    그다지 마음이 당기지 않는 것을 쫓아갔다. 허생원은 계집과는 연분이 멀었다. 얽둑배기 상판을 쳐들고 대어 설 숫기도 없었으나 계집 편에서 정을 보낸 적도 없었고, 쓸쓸하고 뒤틀린 반생이었다. 충줏집을 생각만 하여도 철없이 얼굴이 붉어지고 발밑이 떨리고 그 자리에 소스라쳐버린다. 충줏집 문을 들어서서 술좌석에서 짜장 동이를 만났을 때에는 어찌 된 서슬엔지 발끈 화가 나버렸다. 상위에 붉은 얼굴을 쳐들고 제법 계집과 농탕치는 것을 보고서야 견딜 수 없었던 것이다. 녀석이 제법 난질군인데 꼴사납다. 머리에 피도 안 마른 녀석이 낮부터 술 처먹고 계집과 농탕이야. 장돌뱅이 망신만 시키고 돌아다니누나. 그 꼴에 우리들과 한몫 보자는 셈이지. 동이 앞에 막아서면서부터 책망이었다. 걱정두 팔자요 하는 듯이 빤히 쳐다보는 상기된 눈망울에 부딪칠 때, 얼결김에 따귀를 하나 갈겨주지 않고는 배길 수 없었다. 동이도 화를 쓰고 팩하고 일어서기는 하였으나, 허생원은 조금도 동색하는 법없이 마음먹은 대로는 다 지껄였다--어디서 주워먹은 선머슴인지는 모르겠으나, 네게도 아비 어미 있겠지. 그 사나운 꼴 보면 맘 좋겠다. 장사란 탐탁하게 해야 돼지, 계집이 다 무어야. 나가거라, 냉큼 꼴 치워.
    그러나 한마디도 대거리하지 않고 하염없이 나가는 꼴을 보려니, 도리어 측은히 여겨졌다. 아직두 서름서름한 사인데 너무 과하지 않았을까 하고 마음이 섬짓해졌다. 주제도 넘지, 같은 술손님이면서두 아무리 젊다구 자식 낳게 된 것을 붙들고 치고 닦아 셀 것은 무어야 원. 충줏집은 입술을 쭝긋하고 술 붓는 솜씨도 거칠었으나, 젊은 애들한테는 그것이 약이 된다나 하고 그 자리는 조선달이 얼버무려 넘겼다. 너 녀석한테 반했지? 애숭이를 빨면 죄된다. 한참 법석을 친 후이다. 담도 생긴데다가 웬일인지 흠뻑 취해보고 싶은 생각도 있어서 허생원은 주는 술잔이면 거의 다 들이켰다. 거나해짐을 따라 계집 생각보다도 동이의 뒷일이 한결같이 궁금해졌다. 내 꼴에 계집을 가로채서는 어떡헐 작정이었누 하고 어리석은 꼬락서니를 모질게 책망하는 마음도 한편에 있었다. 그렇기 때문에 얼마나 지난 뒤인지 동이가 헐레벌떡거리며 황급히 부르러 왔을 때에는, 마시던 잔을 그 자리에 던지고 정신없이 허덕이며 충줏집을 뛰어나간 것이다.
    """

    encrypted = core.encrypt(_PLAIN_TEXT, 5, "botchi")
    print(encrypted)


# def test_encrypt_decrypt():
#     original = "Hello, Hachicrypt!"
#     key = "secretkey"
#
#     encrypted = encrypt(original, key)
#     assert encrypted != original, "암호화된 문자열은 원본과 달라야 합니다."
#
#     decrypted = decrypt(encrypted, key)
#     assert decrypted == original, "복호화된 문자열은 원본과 동일해야 합니다."