package chatter;

import chatter.openai.OpenAI;

/**
 * Hello world!
 */
public class App {
    public static void main(String[] args) {
        String key = args[0];
        OpenAI ai = OpenAI.newOpenAI(key);
        String answer = ai.chat("please help me with my exam");
        System.out.println(answer);
    }
}
