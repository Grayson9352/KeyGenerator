import json # i dont think u have to install this
import os
try:
    import pyperclip
except ModuleNotFoundError:
    print("You have to install pyperclip!") # pip install pyperclip
try:
    from googletrans import Translator, constants
except ModuleNotFoundError:
    print("You have to install googletrans!") # pip3 install googletrans==3.1.0a0

#
# TRANSLATING IS NOT ALWAYS WORKING
#

debug = False
def getLang(lang, trans, stra, srcLang=False):
    if debug == False:
        try:
          lang = trans.translate(stra, dest=lang)
        except AttributeError:
            print("""
            PLEASE UNINSTALL GOOGLETRANS AND PUT THIS CMD IN
            pip3 install googletrans==3.1.0a0
            """)
        except:
            print("You have encountered a unexpected error!")
    else:
        try:
            lang = trans.translate(stra, dest=lang, src=srcLang)
        except AttributeError: 
            print("""
            PLEASE UNINSTALL GOOGLETRANS AND PUT THIS CMD IN
            pip3 install googletrans==3.1.0a0
            """)
        except:
            print("You have encountered a unexpected error!")      
    return lang.text

def main():
    translator = Translator()
    preset = input("Please type yes for presets no for no preset: ")
    if preset.lower() == "yes":
        dirOrsame = input("Please type yes for current directory or type the directory for custom directory: ")
        if dirOrsame.lower() == "yes":
            fileLoc = input("Please type the preset file name: ")
            realLoc = "" + os.path.dirname(os.path.realpath(__file__)) + "\\" + fileLoc
            realDir = os.path.isfile("" + os.path.dirname(os.path.realpath(__file__)) + "\\" + fileLoc)
            if realDir == True:
                print("")
                data = json.loads(open(realLoc).read())
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
        if debug == False:
            pass
        else:
            srcPickqr = input("Please select your source")
            srcPick = "\"" + srcPickqr + "\""
        np = "\"" + npqr + "\""
        key = "\"" + keyqr + "\""
        native = "\"" + nativeqr + "\""
        newStr = "\"" + newStrqr + "\""
        if debug == False:
            result = f"+TextReplacements=(Category=Game, bIsMinimalPatch=True, Namespace=" + np +", Key=" + key + ", NativeString=" + native + ", LocalizedStrings=((\"ar\", " + getLang("ar", translator, newStr) + "),(\"en\", " + getLang("en", translator, newStr) + "),(\"de\", " + getLang("de", translator, newStr) + "),(\"es\", " + getLang("es", translator, newStr) + "),(\"es-419\", " + getLang("es", translator, newStr) + "),(\"fr\", " + getLang("fr", translator, newStr) + "),(\"it\", " + getLang("it", translator, newStr) + "),(\"ja\", " + getLang("ja", translator, newStr) + "),(\"ko\", " + getLang("ko", translator, newStr) + "),(\"pl\", " + getLang("pl", translator, newStr) + "),(\"pt-BR\", " + getLang("pt", translator, newStr) + "),(\"ru\", " + getLang("ru", translator, newStr) + "),(\"tr\", " + getLang("tr", translator, newStr) + "),(\"zh-CN\""", " + getLang("zh-CN", translator, newStr) + "),(\"zh-Hant\", " + getLang("zh-CN", translator, newStr) + ")))"
        else:
            result = f"+TextReplacements=(Category=Game, bIsMinimalPatch=True, Namespace=" + np +", Key=" + key + ", NativeString=" + native + ", LocalizedStrings=((\"ar\", " + getLang("ar", translator, newStr, srcPick) + "),(\"en\", " + getLang("en", translator, newStr, srcPick) + "),(\"de\", " + getLang("de", translator, newStr, srcPick) + "),(\"es\", " + getLang("es", translator, newStr, srcPick) + "),(\"es-419\", " + getLang("es", translator, newStr, srcPick) + "),(\"fr\", " + getLang("fr", translator, newStr, srcPick) + "),(\"it\", " + getLang("it", translator, newStr, srcPick) + "),(\"ja\", " + getLang("ja", translator, newStr, srcPick) + "),(\"ko\", " + getLang("ko", translator, newStr, srcPick) + "),(\"pl\", " + getLang("pl", translator, newStr, srcPick) + "),(\"pt-BR\", " + getLang("pt", translator, newStr, srcPick) + "),(\"ru\", " + getLang("ru", translator, newStr, srcPick) + "),(\"tr\", " + getLang("tr", translator, newStr, srcPick) + "),(\"zh-CN\""", " + getLang("zh-CN", translator, newStr, srcPick) + "),(\"zh-Hant\", " + getLang("zh-CN", translator, newStr, srcPick) + ")))"           
        print(result)
        try:
            print("Copied the result!")
            pyperclip.copy(result)
        except:
            print("bruh")
        replay = input("Would you like to generate another one?: ")
        if replay.lower() == "yes":
            main()
        else:
            print("Cancelled")
main()
