package chatter.openai;

import com.theokanning.openai.completion.chat.ChatCompletionRequest;
import com.theokanning.openai.completion.chat.ChatMessage;
import com.theokanning.openai.service.OpenAiService;
import java.util.List;

public class OpenAI {

    private final OpenAiService openAiService;

    private static OpenAI singleton;

    private OpenAI(String key) {
        this.openAiService = new OpenAiService(key);
    }

    public static OpenAI newOpenAI(String key) {
        if (singleton == null) {
            singleton = new OpenAI(key);
        }
        return singleton;
    }

    public String chat(String message) {
        ChatCompletionRequest chatCompletionRequest = ChatCompletionRequest.builder()
            .messages(List.of(new ChatMessage("user", message)))
            .model("gpt-3.5-turbo")
            .user("user")
            .build();
        var result = openAiService.createChatCompletion(chatCompletionRequest);
        return result.getChoices().get(0).getMessage().getContent();
    }
}
