package chatter.persistence;

import java.util.List;
import java.util.stream.Collectors;

import com.theokanning.openai.completion.chat.ChatMessage;

import chatter.model.Conversation;
import chatter.model.ConversationTo;

public class ConversationRepository {

    private static Conversation conversation = new Conversation();

    public static List<ChatMessage> getMessagesOfConversation() {
        return conversation.getMessages();
    }

    public static void addMessageToConversation(ChatMessage message) {
        conversation.addChatMessage(message);
    }

    public static ConversationTo getConversationHistory() {
        ConversationTo conversationTo = new ConversationTo();
        conversationTo.setMessages(conversation.getMessages().stream().map((chatMessage) -> {
            return chatMessage.getRole() + ": " + chatMessage.getContent();
        }).collect(Collectors.toList()));
        return conversationTo;
    }

    public static void resetConversation() {
        conversation.reset();
    }

}
