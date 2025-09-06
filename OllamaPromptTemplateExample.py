from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

load_dotenv()

def load_prompt_template():
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

    summary_template = """
    given the information {information} about a God, I want you to create:
    1) A short summary
    2) Two interesting facts
    3) A short prayer to the God
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    ollamaLLM = ChatOllama(model="gpt-oss:20b", temperature=0)
    chain = summary_prompt_template | ollamaLLM
    response = chain.invoke({"information": information})
    print(response.content)

if __name__ == "__main__":
    load_prompt_template()