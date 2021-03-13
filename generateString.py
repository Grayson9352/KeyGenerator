import json # i dont think u have to install this
import os
import pyperclip # pip install pyperclip
from googletrans import Translator, constants # pip3 install googletrans==3.1.0a0
from pprint import pprint # pip3 install googletrans==3.1.0a0

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
            resultPre = "+TextReplacements=(Category=Game, bIsMinimalPatch=True, Namespace=" + npId +", Key=" + keyId + ", NativeString=" + nativeId + ", LocalizedStrings=((\"ar\", " + newStr1 + "),(\"en\", " + newStr1 + "),(\"de\", " + newStr1 + "),(\"es\", " + newStr1 + "),(\"es-419\", " + newStr1 + "),(\"fr\", " + newStr1 + "),(\"it\", " + newStr1 + "),(\"ja\", " + newStr1 + "),(\"ko\", " + newStr1 + "),(\"pl\", " + newStr1 + "),(\"pt-BR\", " + newStr1 + "),(\"ru\", " + newStr1 + "),(\"tr\", " + newStr1 + "),(\"zh-CN\""", " + newStr1 + "),(\"zh-Hant\", " + newStr1 + ")))"
            print(resultPre)
            print("Copied the result!")
            pyperclip.copy(resultPre)
        else:
            print("That directory is invalid!")
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
            resultPre = "+TextReplacements=(Category=Game, bIsMinimalPatch=True, Namespace=" + npId +", Key=" + keyId + ", NativeString=" + nativeId + ", LocalizedStrings=((\"ar\", " + newStr1 + "),(\"en\", " + newStr1 + "),(\"de\", " + newStr1 + "),(\"es\", " + newStr1 + "),(\"es-419\", " + newStr1 + "),(\"fr\", " + newStr1 + "),(\"it\", " + newStr1 + "),(\"ja\", " + newStr1 + "),(\"ko\", " + newStr1 + "),(\"pl\", " + newStr1 + "),(\"pt-BR\", " + newStr1 + "),(\"ru\", " + newStr1 + "),(\"tr\", " + newStr1 + "),(\"zh-CN\""", " + newStr1 + "),(\"zh-Hant\", " + newStr1 + ")))"
            print(resultPre)
            print("Copied the result!")
            pyperclip.copy(resultPre)
        else:
            print("That directory is invalid!")
else:
    npqr = input("Is there any namespace? Keep empty if none: ")
    keyqr = input("Key: ")
    nativeqr = input("Native: ")
    newStrqr = input("NewText: ")
    np = "\"" + npqr + "\""
    key = "\"" + keyqr + "\""
    native = "\"" + nativeqr + "\""
    newStr = "\"" + newStrqr + "\""
    result = "+TextReplacements=(Category=Game, bIsMinimalPatch=True, Namespace=" + np +", Key=" + key + ", NativeString=" + native + ", LocalizedStrings=((\"ar\", " + translator.translate(newStr, dest="ar").text + "),(\"en\", " + translator.translate(newStr, dest="en").text + "),(\"de\", " + translator.translate(newStr, dest="de").text + "),(\"es\", " + translator.translate(newStr, dest="es").text + "),(\"es-419\", " + translator.translate(newStr, dest="es").text + "),(\"fr\", " + translator.translate(newStr, dest="fr").text + "),(\"it\", " + translator.translate(newStr, dest="it").text + "),(\"ja\", " + translator.translate(newStr, dest="ja").text + "),(\"ko\", " + translator.translate(newStr, dest="ko").text + "),(\"pl\", " + translator.translate(newStr, dest="pl").text + "),(\"pt-BR\", " + translator.translate(newStr, dest="pt").text + "),(\"ru\", " + translator.translate(newStr, dest="ru").text + "),(\"tr\", " + translator.translate(newStr, dest="tr").text + "),(\"zh-CN\""", " + translator.translate("Hello", dest="zh-CN").text + "),(\"zh-Hant\", " + translator.translate("Hello", dest="zh-CN").text + ")))"
    print(result)
    print("Copied the result!")
    pyperclip.copy(result)
