import java.util.Dictionary;
import java.util.Hashtable;
import java.util.Stack;
import java.util.Scanner;

public final class OhaverDecoder {
    static String[] letterCodes = {
        ".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
        "....", "..", ".---", "-.-", ".-..", "--", "-.",
        "---", ".--.", "--.-", ".-.", "...", "-", "..-",
        "...-", ".--", "-..-", "-.--", "--.." 
    };

    static Dictionary<String, Character> decodeDict = getDecodeDict();
    static Dictionary<Character, String> encodeDict = getEncodeDict();

    static private Dictionary<String, Character> getDecodeDict() {
        Dictionary<String, Character> dict = new Hashtable<String, Character>();
        for (int i = 0; i < letterCodes.length; i++) {  // Add all letters
           dict.put(letterCodes[i], (char) ((int) 'A' + i));
        }
        dict.put("..--", '_');
        dict.put("---.", '.');
        dict.put(".-.-", ',');
        dict.put("----", '?'); 
        return dict;
    }

    static private Dictionary<Character, String> getEncodeDict() {
        Dictionary<Character, String> dict = new Hashtable<Character, String>();
        for (int i = 0; i < letterCodes.length; i++) {
            dict.put((char) ((int)'A' + i), letterCodes[i]);
            dict.put('_', "..--");
            dict.put('.', "---.");
            dict.put(',', ".-.-");
            dict.put('?', "----"); 
        }
        return dict;
    }

    static public String decode(String msg) {
        String codes = "";
        Stack<Integer> lens = new Stack<>();
        for (int i = 0; i < msg.length(); i++) {
            char c = msg.charAt(i);
            String code = encodeDict.get(c);
            codes += code;  // Append code to codes
            lens.push(code.length());    // Add the length of the code to the front
        }

        String result = "";
        int startIndex = 0; // Start index of a code
        while (!lens.isEmpty()) {
            int len = lens.pop();
            int endIndex = startIndex + len;    // End index of a code
            String code = codes.substring(startIndex, endIndex);
            char c = decodeDict.get(code);
            result += c;
            startIndex = endIndex;
        }

        return result;
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextLine()){
            String input = sc.nextLine();
            String output = OhaverDecoder.decode(input);
            System.out.println(output);
        }
    }
}