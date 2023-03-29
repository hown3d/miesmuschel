package chatter.openai;

import java.time.Duration;
import java.time.temporal.ChronoUnit;

import com.theokanning.openai.completion.chat.ChatCompletionRequest;
import com.theokanning.openai.completion.chat.ChatMessage;
import com.theokanning.openai.service.OpenAiService;

import chatter.persistence.ConversationRepository;

public class OpenAI {

    private final OpenAiService openAiService;

    private static OpenAI singleton;

    private OpenAI(String key) {
        this.openAiService = new OpenAiService(key, Duration.of(100, ChronoUnit.SECONDS));
    }

    public static OpenAI newOpenAI(String key) {
        if (singleton == null) {
            singleton = new OpenAI(key);
        }
        return singleton;
    }

    public String chat(String message) {
        ConversationRepository.addMessageToConversation(new ChatMessage("user", message));
        ChatCompletionRequest chatCompletionRequest = ChatCompletionRequest.builder()
            .messages(ConversationRepository.getMessagesOfConversation())
            .model("gpt-3.5-turbo")
            .user("user")
            .build();
        var result = this.openAiService.createChatCompletion(chatCompletionRequest);
        ConversationRepository.addMessageToConversation(result.getChoices().get(0).getMessage());

        return result.getChoices().get(0).getMessage().getContent();
    }
}
