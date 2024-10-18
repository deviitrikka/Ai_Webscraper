from  langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

#Langchain allows us to connect LLMs to our python code


#copied this template from a specific 
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

model = OllamaLLM(model="llama3.1")

def parse_with_ollama(dom_chunks, parse_description):
    #when we call an llm we need a prompt
    prompt = ChatPromptTemplate.from_template(template)
    
    #langchain:we have a chain i.e we first gonna go to the prompt and then the model
    chain = prompt | model

    parsed_results = []


    #we pass all our dom content in chunks into LLM and append the results in the parsed_results array
    #i is the index of the current element, chunk is the current element itself
    for i, chunk in enumerate(dom_chunks,start=1):
        #to define/execute a specific function
        response = chain.invoke({"dom_content": chunk,"parse_description": parse_description})

        #to know how many chunks are passing will print it
        print(f"Parsed batch {i} of {len(dom_chunks)}")
        parsed_results.append(response)

    return "\n".join(parsed_results)