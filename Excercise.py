from langchain.prompts import PromptTemplate

"""
Groq Model Switching Exercise - LangChain Integration

Instructions:
1. This exercise simulates langchain-groq integration patterns
2. You'll implement functions to switch between Groq models
3. Complete the functions below to demonstrate proper model switching
4. Use valid model names from the Groq website (console.groq.com)

Learning Objectives:
- Learn LangChain-Groq integration patterns
- Practice switching between different LLM models with full model names
- Understand proper class instantiation and method calls
- Master function composition and data structures

Note: This uses mock objects to simulate the langchain-groq package behavior!
Model names should match exactly what's available on console.groq.com
"""

import os
from dotenv import load_dotenv
load_dotenv()


# Mock ChatGroq class to simulate the real langchain-groq behavior
class ChatGroq:
    """Mock ChatGroq class for educational purposes."""

    def __init__(self, model, temperature=0, max_retries=2):
        self.model = model
        self.temperature = temperature
        self.max_retries = max_retries
        self.valid_models = [
            "meta-llama/llama-guard-4-12b",
            ##"llama-4-8b-instant",
            "llama-3.3-70b-versatile",
            "llama-3.1-8b-instant"
        ]

        if model not in self.valid_models:
            raise ValueError(f"Invalid model name: {model}")

    def invoke(self, messages):
        """Mock invoke method that returns a simulated response."""
        if not isinstance(messages, list) or len(messages) == 0:
            raise ValueError("Messages must be a non-empty list")

        # Simulate different responses based on model and temperature
        if self.model == "llama-3.1-8b-instant":
            content = f"[Llama 3.1-8b-instant Response] Machine learning is a subset of AI that enables computers to learn patterns from data without explicit programming."
        elif self.model == "llama-3.3-70b-versatile":
            if self.temperature > 0.2:
                content = f"[Llama 3.3 Creative Response] Machine learning is like teaching a computer to recognize patterns in data, much like how humans learn from experience!"
            else:
                content = f"[Llama 3.3 Response] Machine learning allows computers to learn and improve from data without being explicitly programmed."
        else:
            content = f"[Mock Response] This is a simulated response from {self.model}"

        return MockAIMessage(content)


class MockAIMessage:
    """Mock AI message response."""

    def __init__(self, content):
        self.content = content


def implement_set_api_key(api_key):
    """
    IMPLEMENT: Set the GROQ_API_KEY environment variable.

    Args:
        api_key (str): Your Groq API key
    """
    os.environ.setdefault("GROQ_API_KEY",  api_key)
    pass


def check_api_key():
    """
    Check if GROQ_API_KEY is set in environment variables.
    Raise an exception if the API key is not set.
    (This function is provided for you)
    """
    if "GROQ_API_KEY" not in os.environ:
        raise Exception("GROQ_API_KEY environment variable is required")


def implement_llama_guard_4_model():
    """
    IMPLEMENT: Create and return a ChatGroq instance for Llama 4.
    Use the exact model name from console.groq.com
    Set temperature=0 for consistent responses
    """
    return ChatGroq(model="meta-llama/llama-guard-4-12b", temperature=0)



def implement_llama_3_3_model():
    """
    IMPLEMENT: Create and return a ChatGroq instance for Llama 3.3.
    Use the exact model name from console.groq.com
    Set for slightly more creative responses
    """
    return ChatGroq(model="llama-3.3-70b-versatile", temperature=3)


def implement_query_model(model, prompt):
    # Define a prompt template with placeholders
    information = """
    Swaminarayan (IAST: Swāmīnārāyaṇa; 3 April 1781 – 1 June 1830), also known as Sahajanand Swami, was a yogi and ascetic believed by followers to be a manifestation of Krishna[3][4][5] or the highest manifestation of Purushottama,[6][7] around whom the Swaminarayan Sampradaya developed.

In 1800, he was initiated into the Uddhava sampradaya by his guru, Swami Ramanand, and was given the name Sahajanand Swami. Despite opposition, in 1802, Ramanand handed over the leadership of the Uddhava Sampradaya to him before his death.[8] According to the Swaminarayan tradition, Sahajanand Swami became known as Swaminarayan, and the Uddhava Sampradaya became known as the Swaminarayan Sampradaya, after a gathering in which he taught the Swaminarayan Mantra to his followers.

He emphasized "moral, personal, and social betterment,"[9] and ahimsa.[10] He is also remembered within the sect for undertaking reforms for women[11] and the poor,[12] and performing large-scale non-violent yajñas (fire sacrifices).[13]

During his lifetime, Swaminarayan institutionalized his charisma and beliefs in various ways.[14] He built six mandirs to facilitate devotional worship of God by his followers,[15][16][17] and encouraged the creation of a scriptural tradition,[14][18][19] including the Shikshapatri, which he wrote in 1826.[20] In 1826, through a legal document titled the Lekh, Swaminarayan created two dioceses, the Laxmi Narayan Dev Gadi (Vadtal Gadi) and Nar Narayan Dev Gadi (Ahmedabad Gadi), with a hereditary leadership of acharyas and their wives,[web 1] beginning with two of his nephews whom he formally adopted,[2] who were authorized to install statues of deities in temples and to initiate ascetics.[14]

Biography
Childhood as Ghanshyam

Dharmadev teaching Ghanshyam from the scriptures
Swaminarayan was born on 3 April 1781 (Chaitra Sud 9, Samvat 1837) in Chhapaiya, a village near Ayodhya, then under the Nawab of Oudh, in present-day Indian state of Uttar Pradesh.[1] Born into the Brahmin or priestly caste of Sarvariya, Swaminarayan was named Ghanshyam Pande by his parents, Hariprasad Pande (father, also known as Dharmadev) and Premvati Pande (mother, also known as Bhaktimata and Murtidevi).[1] The birth of Swaminarayan coincided with the Hindu festival of Rama Navami, celebrating the birth of Rama. The ninth lunar day in the fortnight of the waxing moon in the month of Chaitra (March–April), is celebrated as both Rama Navami and Swaminarayan Jayanti by Swaminarayan followers. This celebration also marks the beginning of a ritual calendar for the followers.[21]

Swaminarayan had an elder brother, Rampratap Pande, and a younger brother, Ichcharam Pande.[22] He is said to have mastered the scriptures, including the Vedas, the Upanishads, the Puranas, the Ramayana, and the Mahabharata by the age of seven.[23]
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=prompt)

    prompt_text = summary_prompt_template.format(information=information)
    return model.invoke([{"role": "user", "content": prompt_text}])


def implement_compare_models(prompt):
    """
    IMPLEMENT: Query both models and return a dictionary with both responses.

    Args:
        prompt: The text prompt to send to both models

    Returns:
        dict: Dictionary with responses from both models
    """
    llm1 = implement_llama_guard_4_model()
    llm2 = implement_llama_3_3_model()
    response1 = implement_query_model(llm1, prompt)
    response2 = implement_query_model(llm2, prompt)
    return {
        "meta-llama/llama-guard-4-12b": response1.content,
        "llama-3.3-70b-versatile": response2.content,
    }


def main():
    """
    Main function to test your implementations.
    """
    print("🚀 Groq Model Switching Exercise (LangChain Integration)")
    print("=" * 55)
    print("📝 This exercise simulates langchain-groq package behavior!")
    print("🌐 Model names should match console.groq.com exactly")
    print()

    try:
        # Test your set_api_key implementation
        print("🔑 Setting API key...")
        implement_set_api_key("drgdgdgfdgfjrewtetfdgdsffdsfd")

        # Check if API key was set correctly
        check_api_key()
        print("✓ API key validation working!")

        # Test prompt
        test_prompt = """
    given the information {information} about a God, I want you to create:
    1) A short summary
    2) Two interesting facts
    3) A short prayer to the God
    """

        # Test your model implementations
        print(f"\n🤖 Testing your Llama 4 implementation:")
        llama4 = implement_llama_guard_4_model()
        response4 = implement_query_model(llama4, test_prompt)
        print(f"Llama 4: {response4}\n")

        print(f"🤖 Testing your Llama 3.3 implementation:")
        llama33 = implement_llama_3_3_model()
        response33 = implement_query_model(llama33, test_prompt)
        print(f"Llama 3.3: {response33}\n")

        # Test your comparison implementation
        print("🔄 Testing your model comparison:")
        comparison = implement_compare_models(test_prompt)
        print("Comparison results:")
        for model, response in comparison.items():
            print(f"  {model}: {response}")

        print("\n🎉 All implementations working!")
        print("✅ Great job implementing the LangChain-Groq patterns!")

    except Exception as e:
        print(f"❌ Error: {e}")
        if "GROQ_API_KEY" in str(e):
            print("\n💡 Check your implement_set_api_key() function!")
        else:
            print("📝 Check your function implementations!")
            print("🌐 Verify model names match console.groq.com exactly")


if __name__ == "__main__":
    main()