package chatter.service.rest.v1;

import chatter.persistence.ConversationRepository;
import io.javalin.Javalin;

public class ConversationService {

    public ConversationService(Javalin app) {
        app.get("chatter/conversation", context -> {
            context.json(ConversationRepository.getConversationHistory());
        });

        app.delete("chatter/conversation", context -> {
            ConversationRepository.resetConversation();
        });
    }
}
