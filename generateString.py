import json
import os
import pyperclip
import googletrans
from googletrans import Translator

#
# TRANSLATING IS NOT ALWAYS WORKING
#

# check googletrans version

if googletrans.__version__ != "3.1.0-alpha":  # this is 3.1.0a0 for some reason
    raise ModuleNotFoundError("""PLEASE USE THE FOLLOWING COMMANDS
    pip3 uninstall googletrans
    pip3 install googletrans==3.1.0a0
            """)

debug = False


def getLang(lang, trans, stra, srcLang=False):
    if not debug:
        try:
            lang = trans.translate(stra, dest=lang)
        except Exception as e:
            print("You have encountered a unexpected error!")
            if input("Send error? (y/n)").lower() == "y":
                print(e)
    else:
        try:
            lang = trans.translate(stra, dest=lang, src=srcLang)
        except Exception as e:
            print("You have encountered a unexpected error!")
            if bool(input("Send error? (y/n)")):
                print(e)
    return lang.text


def main():
    translator = Translator()
    preset = input("Please type yes for presets no for no preset: ")
    if preset.lower() == "yes":
        dirOrSame = input("Please type yes for current directory or type the directory for custom directory: ")
        if dirOrSame.lower() == "yes":
            fileLoc = input("Please type the preset file name: ")
            realLoc = "" + os.path.dirname(os.path.realpath(__file__)) + "\\" + fileLoc
            realDir = os.path.isfile("" + os.path.dirname(os.path.realpath(__file__)) + "\\" + fileLoc)
            if realDir:
                print("")
                data = json.loads(open(realLoc).read())
                presetNameqr = input("What is the preset array name?: ")
                keyId = "\"" + data[presetNameqr]['key_id'] + "\""
                npId = "\"" + data[presetNameqr]['namespace_id'] + "\""
                nativeId = "\"" + data[presetNameqr]['native_id'] + "\""
                newStra1 = input("Please type the name you will replace the string with: ")
                newStr1 = "\"" + newStra1 + "\""
                resultPre = f"+TextReplacements=(Category=Game, bIsMinimalPatch=True, Namespace=" + npId + ", Key=" + keyId + ", NativeString=" + nativeId + ", LocalizedStrings=((\"ar\", " + getLang(
                    "ar", translator, newStr1) + "),(\"en\", " + getLang("en", translator,
                                                                         newStr1) + "),(\"de\", " + getLang("de",
                                                                                                            translator,
                                                                                                            newStr1) + "),(\"es\", " + getLang(
                    "es", translator, newStr1) + "),(\"es-419\", " + getLang("es", translator,
                                                                             newStr1) + "),(\"fr\", " + getLang("fr",
                                                                                                                translator,
                                                                                                                newStr1) + "),(\"it\", " + getLang(
                    "it", translator, newStr1) + "),(\"ja\", " + getLang("ja", translator,
                                                                         newStr1) + "),(\"ko\", " + getLang("ko",
                                                                                                            translator,
                                                                                                            newStr1) + "),(\"pl\", " + getLang(
                    "pl", translator, newStr1) + "),(\"pt-BR\", " + getLang("pt", translator,
                                                                            newStr1) + "),(\"ru\", " + getLang("ru",
                                                                                                               translator,
                                                                                                               newStr1) + "),(\"tr\", " + getLang(
                    "tr", translator, newStr1) + ")))"
                print(resultPre)
                print("Copied the result!")
                pyperclip.copy(resultPre)
            else:
                print("That directory is invalid!")
                main()
        else:
            realDir = os.path.isfile(dirOrSame)
            if realDir:
                print("")
                data = json.loads(open(dirOrSame).read())
                presetNameqr = input("What is the preset array name?: ")
                keyId = "\"" + data[presetNameqr]['key_id'] + "\""
                npId = "\"" + data[presetNameqr]['namespace_id'] + "\""
                nativeId = "\"" + data[presetNameqr]['native_id'] + "\""
                newStra1 = input("Please type the name you will replace the string with: ")
                newStr1 = "\"" + newStra1 + "\""
                resultPre = f"+TextReplacements=(Category=Game, bIsMinimalPatch=True, Namespace=" + npId + ", Key=" + keyId + ", NativeString=" + nativeId + ", LocalizedStrings=((\"ar\", " + getLang(
                    "ar", translator, newStr1) + "),(\"en\", " + getLang("en", translator,
                                                                         newStr1) + "),(\"de\", " + getLang("de",
                                                                                                            translator,
                                                                                                            newStr1) + "),(\"es\", " + getLang(
                    "es", translator, newStr1) + "),(\"es-419\", " + getLang("es", translator,
                                                                             newStr1) + "),(\"fr\", " + getLang("fr",
                                                                                                                translator,
                                                                                                                newStr1) + "),(\"it\", " + getLang(
                    "it", translator, newStr1) + "),(\"ja\", " + getLang("ja", translator,
                                                                         newStr1) + "),(\"ko\", " + getLang("ko",
                                                                                                            translator,
                                                                                                            newStr1) + "),(\"pl\", " + getLang(
                    "pl", translator, newStr1) + "),(\"pt-BR\", " + getLang("pt", translator,
                                                                            newStr1) + "),(\"ru\", " + getLang("ru",
                                                                                                               translator,
                                                                                                               newStr1) + "),(\"tr\", " + getLang(
                    "tr", translator, newStr1) + ")))"
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
        if not debug:
            pass
        else:
            srcPickqr = input("Please select your source")
            srcPick = "\"" + srcPickqr + "\""
        np = "\"" + npqr + "\""
        key = "\"" + keyqr + "\""
        native = "\"" + nativeqr + "\""
        newStr = "\"" + newStrqr + "\""
        if not debug:
            result = f"+TextReplacements=(Category=Game, bIsMinimalPatch=True, Namespace=" + np + ", Key=" + key + ", NativeString=" + native + ", LocalizedStrings=((\"ar\", " + getLang(
                "ar", translator, newStr) + "),(\"en\", " + getLang("en", translator, newStr) + "),(\"de\", " + getLang(
                "de", translator, newStr) + "),(\"es\", " + getLang("es", translator,
                                                                    newStr) + "),(\"es-419\", " + getLang("es",
                                                                                                          translator,
                                                                                                          newStr) + "),(\"fr\", " + getLang(
                "fr", translator, newStr) + "),(\"it\", " + getLang("it", translator, newStr) + "),(\"ja\", " + getLang(
                "ja", translator, newStr) + "),(\"ko\", " + getLang("ko", translator, newStr) + "),(\"pl\", " + getLang(
                "pl", translator, newStr) + "),(\"pt-BR\", " + getLang("pt", translator,
                                                                       newStr) + "),(\"ru\", " + getLang("ru",
                                                                                                         translator,
                                                                                                         newStr) + "),(\"tr\", " + getLang(
                "tr", translator, newStr) + ")))"
        else:
            result = f"+TextReplacements=(Category=Game, bIsMinimalPatch=True, Namespace=" + np + ", Key=" + key + ", NativeString=" + native + ", LocalizedStrings=((\"ar\", " + getLang(
                "ar", translator, newStr, srcPick) + "),(\"en\", " + getLang("en", translator, newStr,
                                                                             srcPick) + "),(\"de\", " + getLang("de",
                                                                                                                translator,
                                                                                                                newStr,
                                                                                                                srcPick) + "),(\"es\", " + getLang(
                "es", translator, newStr, srcPick) + "),(\"es-419\", " + getLang("es", translator, newStr,
                                                                                 srcPick) + "),(\"fr\", " + getLang(
                "fr", translator, newStr, srcPick) + "),(\"it\", " + getLang("it", translator, newStr,
                                                                             srcPick) + "),(\"ja\", " + getLang("ja",
                                                                                                                translator,
                                                                                                                newStr,
                                                                                                                srcPick) + "),(\"ko\", " + getLang(
                "ko", translator, newStr, srcPick) + "),(\"pl\", " + getLang("pl", translator, newStr,
                                                                             srcPick) + "),(\"pt-BR\", " + getLang("pt",
                                                                                                                   translator,
                                                                                                                   newStr,
                                                                                                                   srcPick) + "),(\"ru\", " + getLang(
                "ru", translator, newStr, srcPick) + "),(\"tr\", " + getLang("tr", translator, newStr, srcPick) + ")))"
        print(result)
        try:
            print("Copied the result!")
            pyperclip.copy(result)
        except Exception as e:
            print(e)
        replay = input("Would you like to generate another one? (y/n): ")
        if replay.lower() == "yes":
            main()
        else:
            print("Cancelled")


main()
