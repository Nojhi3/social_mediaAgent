from langchain.tools import BaseTool
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document
from typing import Optional, Type, Any
from pydantic import BaseModel, Field
import os


class ContentRetrieverInput(BaseModel):
    query: str = Field(description="Search query to find relevant past content")


class ContentRetrieverTool(BaseTool):
    name = "content_retriever"
    description = "Retrieves previously generated content ideas and captions from the knowledge base. Use this to reference past content or find similar ideas."
    args_schema: Type[BaseModel] = ContentRetrieverInput
    embedding_function: Any = None
    vectorstore: Any = None
    
    def __init__(self):
        super().__init__()
        self.embedding_function = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        persist_directory = "./chroma_db"

        os.makedirs(persist_directory, exist_ok=True)
        
        self.vectorstore = Chroma(
            collection_name="social_media_content",
            embedding_function=self.embedding_function,
            persist_directory=persist_directory
        )

        self._initialize_sample_data()
    
    def _initialize_sample_data(self):
        """Initialize with sample social media content"""
        try:
            existing_docs = self.vectorstore.get()
            if len(existing_docs['ids']) == 0:
                sample_docs = [
                    Document(
                        page_content="AI trends in 2025: Focus on generative AI tools for content creation",
                        metadata={"type": "idea", "platform": "LinkedIn", "niche": "AI"}
                    ),
                    Document(
                        page_content="Behind-the-scenes of our product development process",
                        metadata={"type": "idea", "platform": "Instagram", "niche": "Tech"}
                    ),
                    Document(
                        page_content="Customer success story highlighting how our solution solved real problems",
                        metadata={"type": "idea", "platform": "LinkedIn", "niche": "SaaS"}
                    ),
                ]
                self.vectorstore.add_documents(sample_docs)
        except:
            pass
    
    def _run(self, query: str) -> str:
        """Retrieve relevant content from knowledge base"""
        try:
            results = self.vectorstore.similarity_search(query, k=3)
            if results:
                output = "Found relevant past content:\n\n"
                for i, doc in enumerate(results, 1):
                    output += f"{i}. {doc.page_content}\n"
                    output += f"   Platform: {doc.metadata.get('platform', 'N/A')}, "
                    output += f"Niche: {doc.metadata.get('niche', 'N/A')}\n\n"
                return output
            else:
                return "No relevant past content found in the knowledge base."
        except Exception as e:
            return f"Error retrieving content: {str(e)}"
    
    async def _arun(self, query: str) -> str:
        raise NotImplementedError("Async not implemented")
    
    def add_content(self, content: str, metadata: dict):
        """Add new content to the knowledge base"""
        doc = Document(page_content=content, metadata=metadata)
        self.vectorstore.add_documents([doc])
