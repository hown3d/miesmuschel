package chatter.model;

import java.util.ArrayList;
import java.util.List;

import com.theokanning.openai.completion.chat.ChatMessage;

public class Conversation {

    private List<ChatMessage> messages;

    public Conversation() {
        this.messages = new ArrayList<>();
    }

    public void addChatMessage(ChatMessage message) {
        this.messages.add(message);
    }

    public List<ChatMessage> getMessages() {
        return this.messages;
    }

    public void reset() {
        this.messages.clear();
    }
}
