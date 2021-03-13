import json # i dont think u have to install this
import os
import pyperclip # pip install pyperclip
from googletrans import Translator, constants # pip3 install googletrans==3.1.0a0
# from pprint import pprint # pip3 install googletrans==3.1.0a0

#
# TRANSLATING IS NOT ALWAYS WORKING
#


def getLang(lang, trans, stra):
    lang = trans.translate(stra, dest=lang)
    return lang.text

def main():
    translator = Translator()
    preset = input("Please type yes for presets no for no preset: ")
    if preset.lower() == "yes":
        dirOrsame = input("Please type yes for current directory or type the directory for custom directory: ")
        if dirOrsame.lower() == "yes":
            fileLoc = input("Please type the preset file name: ")
            currentDir = os.path.dirname(os.path.realpath(__file__))
            realDir = os.path.isfile("" + currentDir + "\\" + fileLoc)
            if realDir == True:
                print("")
                data = json.loads(open(fileLoc).read())
                presetNameqr = input("What is the preset array name?: ")
                keyId = "\"" + data[presetNameqr]['key_id'] + "\""
                npId = "\"" + data[presetNameqr]['namespace_id'] + "\""
                nativeId = "\"" + data[presetNameqr]['native_id'] + "\""
                newStra1 = input("Please type the name you will replace the string with: ")
                newStr1 = "\"" + newStra1 + "\""
                resultPre = f"+TextReplacements=(Category=Game, bIsMinimalPatch=True, Namespace=" + npId +", Key=" + keyId + ", NativeString=" + nativeId + ", LocalizedStrings=((\"ar\", " + getLang("ar", translator, newStr1) + "),(\"en\", " + getLang("en", translator, newStr1) + "),(\"de\", " + getLang("de", translator, newStr1) + "),(\"es\", " + getLang("es", translator, newStr1) + "),(\"es-419\", " + getLang("es", translator, newStr1) + "),(\"fr\", " + getLang("fr", translator, newStr1) + "),(\"it\", " + getLang("it", translator, newStr1) + "),(\"ja\", " + getLang("ja", translator, newStr1) + "),(\"ko\", " + getLang("ko", translator, newStr1) + "),(\"pl\", " + getLang("pl", translator, newStr1) + "),(\"pt-BR\", " + getLang("pt", translator, newStr1) + "),(\"ru\", " + getLang("ru", translator, newStr1) + "),(\"tr\", " + getLang("tr", translator, newStr1) + "),(\"zh-CN\""", " + getLang("zh-CN", translator, newStr1) + "),(\"zh-Hant\", " + getLang("zh-CN", translator, newStr1) + ")))"
                print(resultPre)
                print("Copied the result!")
                pyperclip.copy(resultPre)
            else:
                print("That directory is invalid!")
                main()
        else:
            # fileLoc = input("Please type the preset file name: ")
            realDir = os.path.isfile(dirOrsame)
            if realDir == True:
                print("")
                data = json.loads(open(dirOrsame).read())
                presetNameqr = input("What is the preset array name?: ")
                keyId = "\"" + data[presetNameqr]['key_id'] + "\""
                npId = "\"" + data[presetNameqr]['namespace_id'] + "\""
                nativeId = "\"" + data[presetNameqr]['native_id'] + "\""
                newStra1 = input("Please type the name you will replace the string with: ")
                newStr1 = "\"" + newStra1 + "\""
                resultPre = f"+TextReplacements=(Category=Game, bIsMinimalPatch=True, Namespace=" + npId +", Key=" + keyId + ", NativeString=" + nativeId + ", LocalizedStrings=((\"ar\", " + getLang("ar", translator, newStr1) + "),(\"en\", " + getLang("en", translator, newStr1) + "),(\"de\", " + getLang("de", translator, newStr1) + "),(\"es\", " + getLang("es", translator, newStr1) + "),(\"es-419\", " + getLang("es", translator, newStr1) + "),(\"fr\", " + getLang("fr", translator, newStr1) + "),(\"it\", " + getLang("it", translator, newStr1) + "),(\"ja\", " + getLang("ja", translator, newStr1) + "),(\"ko\", " + getLang("ko", translator, newStr1) + "),(\"pl\", " + getLang("pl", translator, newStr1) + "),(\"pt-BR\", " + getLang("pt", translator, newStr1) + "),(\"ru\", " + getLang("ru", translator, newStr1) + "),(\"tr\", " + getLang("tr", translator, newStr1) + "),(\"zh-CN\""", " + getLang("zh-CN", translator, newStr1) + "),(\"zh-Hant\", " + getLang("zh-CN", translator, newStr1) + ")))"
                print(resultPre)
                print("Copied the result!")
                pyperclip.copy(resultPre)
                replay = input("Would you like to generate another one?: ")
                if replay.lower() == "yes":
                    main()
                else:
                    print("Cancelled")
            else:
                print("That directory is invalid!")
                main()
    else:
        npqr = input("Is there any namespace? Keep empty if none: ")
        keyqr = input("Key: ")
        nativeqr = input("Native: ")
        newStrqr = input("NewText: ")
        np = "\"" + npqr + "\""
        key = "\"" + keyqr + "\""
        native = "\"" + nativeqr + "\""
        newStr = "\"" + newStrqr + "\""
        result = f"+TextReplacements=(Category=Game, bIsMinimalPatch=True, Namespace=" + np +", Key=" + key + ", NativeString=" + native + ", LocalizedStrings=((\"ar\", " + getLang("ar", translator, newStr) + "),(\"en\", " + getLang("en", translator, newStr) + "),(\"de\", " + getLang("de", translator, newStr) + "),(\"es\", " + getLang("es", translator, newStr) + "),(\"es-419\", " + getLang("es", translator, newStr) + "),(\"fr\", " + getLang("fr", translator, newStr) + "),(\"it\", " + getLang("it", translator, newStr) + "),(\"ja\", " + getLang("ja", translator, newStr) + "),(\"ko\", " + getLang("ko", translator, newStr) + "),(\"pl\", " + getLang("pl", translator, newStr) + "),(\"pt-BR\", " + getLang("pt", translator, newStr) + "),(\"ru\", " + getLang("ru", translator, newStr) + "),(\"tr\", " + getLang("tr", translator, newStr) + "),(\"zh-CN\""", " + getLang("zh-CN", translator, newStr) + "),(\"zh-Hant\", " + getLang("zh-CN", translator, newStr) + ")))"
        print(result)
        print("Copied the result!")
        pyperclip.copy(result)
        replay = input("Would you like to generate another one?: ")
        if replay.lower() == "yes":
            main()
        else:
            print("Cancelled")
main()
