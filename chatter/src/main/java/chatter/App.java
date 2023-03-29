package chatter;

import chatter.openai.OpenAI;
import chatter.service.rest.v1.ConversationService;
import chatter.service.rest.v1.MessageService;
import io.javalin.Javalin;

/**
 * Hello world!
 */
public class App {
    public static void main(String[] args) {

        String key = args[0];
        OpenAI ai = OpenAI.newOpenAI(key);
        Javalin app = Javalin.create();
        new MessageService(ai, app);
        new ConversationService(app);
        app.start(8080);
    }
}
