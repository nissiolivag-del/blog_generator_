from langchain_core.prompts import PromptTemplate
blog_prompt = PromptTemplate(
    input_variables=["topic","tone","length","audience"],
    template="""
    Include:
    Catchy Title
    Introduction
    4-5 headings
    Practical examples
    Conclusion
    Key takeaways
    Return the response in Markdowm.
    """
)