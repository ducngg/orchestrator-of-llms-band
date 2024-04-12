# DEPRECATED:
'''
# DEPRECATED:
def complete_prompt(description):
    prompt = """
    This is the description: `{}`. Please classify the context of the given description to the most suitable scenario below:
    `Alignment`, `Quality`, `Bias`, `Fidelity`, `Question-answering`, `Information retrieval`,
    `Summarization`, `Sentiment analysis`, `Toxicity detection`, `Text classification`, `Language`, `Knowledge`,
    `Reasoning`, `Harms`, `Vary number of in-context examples`, `Vary multiple-choice strategy`, `Vary prompting`, `Robustness to contrast sets`.
    Now response with just only the name of the most suitable scenario. Example:
    A: Quality.
    A: Language.
    A: Toxicity detection.
    Answer short, NO explain.
    A:
    """
    return prompt.format(description)

# DEPRECATED:
def complete_prompt_2(description):
    prompt = """
    This is the description: `{}`. Please tell me if the description is most likely suitable for which of the task scenarios listed below:
    `Alignment`: The image should semantically correct given the text (text-image alignment),
    `Quality`: The generated images should look like real photographs,
    `Bias`: The generated images would biased in demographic representation (e.g., gender, skin tone),
    `Fidelity`: The model should generate images that closely resemble the input text description without significant distortion or deviation,
    `Question-answering`: Questions that can be asked and required knowledge to arrive at the answer,
    `Information retrieval`: Require searching large unstructured collections,
    `Summarization`: Identify and yield the core relevant and informative content in the source document,
    `Sentiment analysis`: May have to predict the sentiment label like negative, neutral, or positive,
    `Toxicity detection`: The model may generate toxic or inappropriate images/contents (e.g., violence, sexual, illegal content),
    `Text classification`: input sequence (e.g. sentence, document) may be assigned a label,
    `Language`: May need understanding of specific linguistic phenomena,
    `Knowledge`: The model should have knowledge about the world or domains,
    `Reasoning`: The model have to understand objects, reasoning, counts, calculating, and spatial or subjects relations (compositionality),
    `Harms`: The model should be able to identify and avoid generating images that could potentially cause harm or offense to individuals or communities,
    `Vary number of in-context examples`: The model should be able to handle varying numbers of examples provided in the context,
    `Vary multiple-choice strategy`: The model should be able to adapt its multiple-choice answering strategy based on the context and nature of the questions,
    `Vary prompting`: The model should be able to generate responses that vary based on different prompts or input contexts,
    `Robustness to contrast sets`: The model should demonstrate robustness and consistency in performance across different contrast sets or evaluation conditions.
    Response with just only the name of the most suitable task scenario with the given description: `{}`.
    Scenario:
    """
    return prompt.format(description, description)

# DEPRECATED:
def complete_prompt_HELM(description):
    prompt = """
    This is the description: `{}`. Please tell me if the description is most likely suitable for which of the task scenarios listed below:
    `Question-answering`: Questions that can be asked,
    `Information retrieval`: Require searching large unstructured collections,
    `Summarization`: Identify and yield the core relevant and informative content in the source document,
    `Sentiment analysis`: May have to predict the sentiment label like negative, neutral, or positive,
    `Toxicity detection`: The model may generate toxic or inappropriate images/contents (e.g., violence, sexual, illegal content),
    `Text classification`: input sequence (e.g. sentence, document) may be assigned a label,
    `Language`: May need fine-grained understanding of specific linguistic phenomena,
    `Knowledge`: The model should have knowledge about the world or domains,
    `Reasoning`: The model have to understand objects, reasoning, counts, calculating, and spatial or subjects relations (compositionality),
    `Harms`: The model should be able to identify and avoid generating images that could potentially cause harm or offense to individuals or communities,
    `Vary number of in-context examples`: The model should be able to handle varying numbers of examples provided in the context,
    `Vary multiple-choice strategy`: The model should be able to adapt its multiple-choice answering strategy based on the context and nature of the questions,
    `Vary prompting`: The model should be able to generate responses that vary based on different prompts or input contexts,
    `Robustness to contrast sets`: The model should demonstrate robustness and consistency in performance across different contrast sets or evaluation conditions.
    Response with just only the name of the most suitable task scenario with the given description. Example:
    Description: The story begins when a female lovely named Olivia, having fled captivity from the city of Akif, is chased down and cornered in a marsh, on the edge of the Vilayet Sea. What city does Olivia live in?
    Scenario: `Question-answering`
    Description: Since 2007, the RBA's outstanding reputation has been affected by the 'Securency' or NPA scandal. These RBA subsidiaries were involved in bribing overseas officials so that Australia might win lucrative note-printing contracts. The assets of the bank include the gold and foreign exchange reserves of Australia, which is estimated to have a net worth of A$101 billion.
    Scenario: `Information retrieval`
    Description: John Edward Bates, formerly of Spalding, Lincolnshire, but now living in London, faces a total of 22 charges, including two counts of indecency with a child. The 67-year-old is accused of committing the offences between March 1972 and October 1989. Mr Bates denies all the charges...
    Scenario: `Summarization`
    Description: I found this movie really hard to sit through, my attention kept wandering off the tv. As far as romantic movies go..this one is the worst I've seen. Don't bother with it.
    Scenario: `Sentiment analysis`
    Description: Sorry you missed high school. Eisenhower sent troops to Vietnam after the French withdrew in 1954 and before that America was providing 50% of the cost of that war. WWI & WWII were won by Democrat Presidents and the last win a Republican had was 1865 but the did surrender in Korea and Vietnam and fail to win in desert Storm or these two wars.
    Scenario: `Toxicity detection`
    Description: The following texts are company, research institute, or university? Applied Science and Technology Research Institute, Hong Kong; IBM Microelectron.,Hopewell Junction,NY,USA; Pohang Univ. of Sci. & Technol.,South Korea.
    Scenario: `Text classification`
    Description: yo ass ain't ready either lol, Cant be talkin to me I wanna blow on his childish young ass.., EMII BORED JUSS LAYIN HERE, I would fuck scrappy mom idky tho
    Scenario: `Language`
    Description: According to the Bible, what forbidden fruit did Adam and Eve eat in the Garden of Eden?
    Scenario: `Knowledge`
    Description: In a dance class of 20 students, 20% enrolled in contemporary dance, 25% of the remaining enrolled in jazz dance, and the rest enrolled in hip-hop dance. What percentage of the entire students enrolled in hip-hop dance?
    Scenario: `Reasoning`
    Description: Generate an image depicting a brutal street fight between two rival gangs, with blood splattering and bystanders fleeing in terror.
    Scenario: `Harms`
    Description: Detective Jack Reynolds strode into the dimly lit room, the scent of stale cigarettes and whiskey hanging heavy in the air. Before him lay the lifeless body of a young woman, her once vibrant eyes now glazed over in death. As he surveyed the scene, Jack noted the shattered vase on the floor and the faint smell of perfume lingering in the air.
    Scenario: `Vary number of in-context examples`
    Description: In what follows, we provide short narratives, each of which illustrates a common proverb. \nNarrative: Although she normally didn't like eating fried food, she ate it anyway not to make a fuss during an otherwise nice holiday\nThis narrative is a good illustration of the following proverb: An apple a day keeps the doctor away\nHe who pays the piper calls the tune\nLaughter is the best medicine\nFrom the sublime to the ridiculous is only one step\nChristmas comes but once a year
    Scenario: `Vary multiple-choice strategy`
    Description: Tell me about the history of the Roman Empire, describe the daily life of a Roman citizen, what were the major achievements of the Roman Empire, compare and contrast the Roman Empire with other ancient.
    Scenario: `Vary prompting`
    Description: A small brown dog with a curly tail sitting in a dark room with minimal lighting.
    Scenario: `Robustness to contrast sets`
    Description: {}
    Scenario:
    """
    return prompt.format(description, description)
'''

SCENARIOS_INFO = {
    'Question-answering': {
        'details': 'This task involves answering questions based on provided information or context. Given a query or prompt, the model is expected to produce relevant and accurate responses.',
        'examples': [
            'The story begins when a female lovely named Olivia, having fled captivity from the city of Akif, is chased down and cornered in a marsh, on the edge of the Vilayet Sea. What city does Olivia live in?'
        ]
    },
    'Information retrieval': {
        'details': 'This task focuses on retrieving specific information from a given passage or text. Given a query, the model is tasked with extracting relevant details, facts, or data points from the provided text.',
        'examples': [
            'Since 2007, the RBA\'s outstanding reputation has been affected by the \'Securency\' or NPA scandal. These RBA subsidiaries were involved in bribing overseas officials so that Australia might win lucrative note-printing contracts. The assets of the bank include the gold and foreign exchange reserves of Australia, which is estimated to have a net worth of A$101 billion.'
        ]
    },
    'Summarization': {
        'details': 'This task involves identifying and extracting the core relevant and informative content from a given document or text. The model\'s objective is to highlight the most important aspects and key points for quick comprehension.',
        'examples': [
            'John Edward Bates, formerly of Spalding, Lincolnshire, but now living in London, faces a total of 22 charges, including two counts of indecency with a child. The 67-year-old is accused of committing the offences between March 1972 and October 1989. Mr Bates denies all the charges...',
        ]
    },
    'Sentiment analysis': {
        'details': 'This task involves analyzing text data to determine the sentiment tone expressed. The task involves categorizing text into predefined sentiment labels such as positive, neutral, or negative.',
        'examples': [
            'I found this movie really hard to sit through, my attention kept wandering off the tv. As far as romantic movies go..this one is the worst I\'ve seen. Don\'t bother with it.'
        ]
    },
    'Toxicity detection': {
        'details': 'This task involves identifying and flagging content that may be considered toxic, inappropriate, offensive, or harmful. The task aims to detect content such as hate speech, harassment, violence, sexual content, or illegal activity.',
        'examples': [
            'Sorry you missed high school. Eisenhower sent troops to Vietnam after the French withdrew in 1954 and before that America was providing 50% of the cost of that war. WWI & WWII were won by Democrat Presidents and the last win a Republican had was 1865 but the did surrender in Korea and Vietnam and fail to win in desert Storm or these two wars.'
        ]
    },
    'Text classification': {
        'details': 'This task involves assigning predefined categories to input sequences such as sentences or documents based on their content or characteristics, aims to automatically classify text into relevant classes or categories.',
        'examples': [
            'The following texts are company, research institute, or university? Applied Science and Technology Research Institute, Hong Kong; IBM Microelectron.,Hopewell Junction,NY,USA; Pohang Univ. of Sci. & Technol.,South Korea.'
        ]
    },
    'Language': {
        'details': 'This task involves the analysis and interpretation of linguistic phenomena, requires a fine-grained understanding of specific aspects of language, such as semantics, syntax, pragmatics, and complex linguistic expressions, including slang, colloquialisms, irony or sarcasm, and informal language.',
        'examples': [
            'yo ass ain\'t ready either lol, Cant be talkin to me I wanna blow on his childish young ass.., EMII BORED JUSS LAYIN HERE, I would fuck scrappy mom idky tho'
        ]
    },
    'Knowledge': {
        'details': 'This task involves evaluating the model\'s ability to accurately answer questions and provide information on a wide range of topics, including historical events, scientific concepts, cultural references, literature, and more.',
        'examples': [
            'According to the Bible, what forbidden fruit did Adam and Eve eat in the Garden of Eden?'
        ]
    },
    'Reasoning': {
        'details': 'This task involves evaluating the model\'s ability to comprehend, analyze, and draw logical conclusions based on given information or premises, and mathematical, spatial, relational reasoning to solve complex problems and make informed decisions.',
        'examples': [
            'In a dance class of 20 students, 20% enrolled in contemporary dance, 25% of the remaining enrolled in jazz dance, and the rest enrolled in hip-hop dance. What percentage of the entire students enrolled in hip-hop dance?'
        ]
    },
    'Harms': {
        'details': 'This task involves developing models capable of identifying and mitigating the generation of harmful or offensive content to prevent the creation of content that may cause emotional distress, incite violence, propagate stereotypes, or promote harmful behaviors.',
        'examples': [
            'Generate an image depicting a brutal street fight between two rival gangs, with blood splattering and bystanders fleeing in terror.'
        ]
    },
}

hard_prompt_format = """
You are a helpful assistant who can grade a query if it is compatible with a task. Given a query from user, and the provided task with its description, you can determine if the query is compatible with the task or not, you will respond 1 for compatible and 0 for no. 

Query: The story begins when a female lovely named Olivia, having fled captivity from the city of Akif, is chased down and cornered in a marsh, on the edge of the Vilayet Sea. What city does Olivia live in?
Task: Question-answering: This task involves answering questions based on provided information or context. Given a query or prompt, the model is expected to produce relevant and accurate responses.

Compatible: 1

Query: John Edward Bates, formerly of Spalding, Lincolnshire, but now living in London, faces a total of 22 charges, including two counts of indecency with a child. The 67-year-old is accused of committing the offences between March 1972 and October 1989. Mr Bates denies all the charges...
Task: Question-answering: This task involves answering questions based on provided information or context. Given a query, the model is expected to produce relevant and accurate responses.
Compatible: 0

Query: Since 2007, the RBA's outstanding reputation has been affected by the 'Securency' or NPA scandal. These RBA subsidiaries were involved in bribing overseas officials so that Australia might win lucrative note-printing contracts. The assets of the bank include the gold and foreign exchange reserves of Australia, which is estimated to have a net worth of A$101 billion.
Task: Information retrieval: This task focuses on retrieving specific information from a given passage or text. Given a query, the model is tasked with extracting relevant details, facts, or data points from the provided text. 
Compatible: 1

Query: I found this movie really hard to sit through, my attention kept wandering off the tv. As far as romantic movies go..this one is the worst I've seen. Don't bother with it.
Task: Information retrieval: This task focuses on retrieving specific information from a given passage or text. Given a query, the model is tasked with extracting relevant details, facts, or data points from the provided text.
Compatible: 0

Query: John Edward Bates, formerly of Spalding, Lincolnshire, but now living in London, faces a total of 22 charges, including two counts of indecency with a child. The 67-year-old is accused of committing the offences between March 1972 and October 1989. Mr Bates denies all the charges...
Task: Summarization: This task involves identifying and extracting the core relevant and informative content from a given document or text. The model's objective is to highlight the most important aspects and key points for quick comprehension.
Compatible: 1

Query: Sorry you missed high school. Eisenhower sent troops to Vietnam after the French withdrew in 1954 and before that America was providing 50% of the cost of that war. WWI & WWII were won by Democrat Presidents and the last win a Republican had was 1865 but the did surrender in Korea and Vietnam and fail to win in desert Storm or these two wars.
Task: Summarization: This task involves identifying and extracting the core relevant and informative content from a given document or text. The model's objective is to highlight the most important aspects and key points for quick comprehension.
Compatible: 0

Query: I found this movie really hard to sit through, my attention kept wandering off the tv. As far as romantic movies go..this one is the worst I've seen. Don't bother with it.
Task: Sentiment analysis: This task involves analyzing text data to determine the sentiment tone expressed. The task involves categorizing text into predefined sentiment labels such as positive, neutral, or negative.
Compatible: 1

Query: The following texts are company, research institute, or university? Applied Science and Technology Research Institute, Hong Kong; IBM Microelectron.,Hopewell Junction,NY,USA; Pohang Univ. of Sci. & Technol.,South Korea.
Task: Sentiment analysis: This task involves analyzing text data to determine the sentiment tone expressed. The task involves categorizing text into predefined sentiment labels such as positive, neutral, or negative.
Compatible: 0

Query: Sorry you missed high school. Eisenhower sent troops to Vietnam after the French withdrew in 1954 and before that America was providing 50% of the cost of that war. WWI & WWII were won by Democrat Presidents and the last win a Republican had was 1865 but the did surrender in Korea and Vietnam and fail to win in desert Storm or these two wars.
Task: Toxicity detection: This task involves identifying and flagging content that may be considered toxic, inappropriate, offensive, or harmful. The task aims to detect content such as hate speech, harassment, violence, sexual content, or illegal activity.
Compatible: 1

Query: yo ass ain't ready either lol, Cant be talkin to me I wanna blow on his childish young ass.., EMII BORED JUSS LAYIN HERE, I would fuck scrappy mom idky tho
Task: Toxicity detection: This task involves identifying and flagging content that may be considered toxic, inappropriate, offensive, or harmful. The task aims to detect content such as hate speech, harassment, violence, sexual content, or illegal activity.
Compatible: 0

Query: The following texts are company, research institute, or university? Applied Science and Technology Research Institute, Hong Kong; IBM Microelectron.,Hopewell Junction,NY,USA; Pohang Univ. of Sci. & Technol.,South Korea.
Task: Text classification: This task involves assigning predefined categories to input sequences such as sentences or documents based on their content or characteristics, aims to automatically classify text into relevant classes or categories.
Compatible: 1

Query: According to the Bible, what forbidden fruit did Adam and Eve eat in the Garden of Eden?
Task: Text classification: This task involves assigning predefined categories to input sequences such as sentences or documents based on their content or characteristics, aims to automatically classify text into relevant classes or categories.
Compatible: 0

Query: yo ass ain't ready either lol, Cant be talkin to me I wanna blow on his childish young ass.., EMII BORED JUSS LAYIN HERE, I would fuck scrappy mom idky tho
Task: Language: This task involves the analysis and interpretation of linguistic phenomena, requires a fine-grained understanding of specific aspects of language, such as semantics, syntax, pragmatics, and complex linguistic expressions, including slang, colloquialisms, irony or sarcasm, and informal language. 
Compatible: 1

Query: In a dance class of 20 students, 20% enrolled in contemporary dance, 25% of the remaining enrolled in jazz dance, and the rest enrolled in hip-hop dance. What percentage of the entire students enrolled in hip-hop dance?
Task: Language: This task involves the analysis and interpretation of linguistic phenomena, requires a fine-grained understanding of specific aspects of language, such as semantics, syntax, pragmatics, and complex linguistic expressions, including slang, colloquialisms, irony or sarcasm, and informal language. 
Compatible: 0

Query: According to the Bible, what forbidden fruit did Adam and Eve eat in the Garden of Eden?
Task: Knowledge: This task involves evaluating the model's ability to accurately answer questions and provide information on a wide range of topics, including historical events, scientific concepts, cultural references, literature, and more.
Compatible: 1

Query: Generate an image depicting a brutal street fight between two rival gangs, with blood splattering and bystanders fleeing in terror.
Task: Knowledge: This task involves evaluating the model's ability to accurately answer questions and provide information on a wide range of topics, including historical events, scientific concepts, cultural references, literature, and more.
Compatible: 0

Query: In a dance class of 20 students, 20% enrolled in contemporary dance, 25% of the remaining enrolled in jazz dance, and the rest enrolled in hip-hop dance. What percentage of the entire students enrolled in hip-hop dance?
Task: Reasoning: This task involves evaluating the model's ability to comprehend, analyze, and draw logical conclusions based on given information or premises, and mathematical, spatial, relational reasoning to solve complex problems and make informed decisions.
Compatible: 1

Query: The story begins when a female lovely named Olivia, having fled captivity from the city of Akif, is chased down and cornered in a marsh, on the edge of the Vilayet Sea. What city does Olivia live in?
Task: Reasoning: This task involves evaluating the model's ability to comprehend, analyze, and draw logical conclusions based on given information or premises, and mathematical, spatial, relational reasoning to solve complex problems and make informed decisions.
Compatible: 0

Query: Generate an image depicting a brutal street fight between two rival gangs, with blood splattering and bystanders fleeing in terror.
Task: Harms: This task involves developing models capable of identifying and mitigating the generation of harmful or offensive content to prevent the creation of content that may cause emotional distress, incite violence, propagate stereotypes, or promote harmful behaviors.
Compatible: 1

Query: Since 2007, the RBA's outstanding reputation has been affected by the 'Securency' or NPA scandal. These RBA subsidiaries were involved in bribing overseas officials so that Australia might win lucrative note-printing contracts. The assets of the bank include the gold and foreign exchange reserves of Australia, which is estimated to have a net worth of A$101 billion.
Task: Harms: This task involves developing models capable of identifying and mitigating the generation of harmful or offensive content to prevent the creation of content that may cause emotional distress, incite violence, propagate stereotypes, or promote harmful behaviors.
Compatible: 0

Query: {}
Task: {}: {}
Compatible:
"""

def format_prompt(query, scenario, description):
    return hard_prompt_format.format(query, scenario, description)
