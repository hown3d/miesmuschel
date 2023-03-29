package chatter.service.rest.v1;

import chatter.model.MessageTo;
import chatter.openai.OpenAI;
import io.javalin.Javalin;

public class MessageService {

    public MessageService(OpenAI ai, Javalin app) {
        app.get("/chatter/message", (context -> {
            MessageTo message = context.bodyAsClass(MessageTo.class);
            context.result(ai.chat(message.getMessage()));
        }));
    }

}
