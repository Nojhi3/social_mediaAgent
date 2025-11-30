from langchain.tools import BaseTool
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from typing import Optional, Type, Any
from pydantic import BaseModel, Field


class ContentIdeaInput(BaseModel):
    query: str = Field(description="The topic or theme for content ideas")


class ContentIdeaTool(BaseTool):
    name = "content_idea_generator"
    description = "Generates creative social media content ideas based on a given topic, niche, or theme. Use this when users ask for content ideas, post suggestions, or creative inspiration."
    args_schema: Type[BaseModel] = ContentIdeaInput
    llm_instance: Any = None
    
    def __init__(self, llm):
        super().__init__()
        self.llm_instance = llm
        
    def _run(self, query: str) -> str:
        """Generate content ideas"""
        prompt = PromptTemplate(
            input_variables=["topic"],
            template="""You are a creative social media strategist. Generate 5 unique and engaging content ideas for the following topic:

Topic: {topic}

For each idea, provide:
1. A catchy title
2. Brief description (1-2 sentences)
3. Suggested platform (Instagram, Twitter, LinkedIn, TikTok, etc.)
4. Content format (carousel, video, image, text post, etc.)

Format your response as a numbered list."""
        )
        chain = LLMChain(llm=self.llm_instance, prompt=prompt)
        return chain.run(topic=query)
    
    async def _arun(self, query: str) -> str:
        raise NotImplementedError("Async not implemented")


class CaptionInput(BaseModel):
    query: str = Field(description="The content idea to generate captions for")


class CaptionGeneratorTool(BaseTool):
    name = "caption_generator"
    description = "Generates engaging social media captions for posts. Use this when users need captions, copy, or post text for their content ideas."
    args_schema: Type[BaseModel] = CaptionInput
    llm_instance: Any = None
    
    def __init__(self, llm):
        super().__init__()
        self.llm_instance = llm
        
    def _run(self, query: str) -> str:
        """Generate social media caption"""
        prompt = PromptTemplate(
            input_variables=["idea"],
            template="""You are an expert social media copywriter. Create an engaging caption for the following content idea:

Content Idea: {idea}

Generate 3 different caption variations:
1. Short & punchy (suitable for Twitter/Instagram)
2. Medium length with storytelling (suitable for LinkedIn/Facebook)
3. Long-form with call-to-action (suitable for blog posts/LinkedIn articles)

Include relevant hashtags and emojis where appropriate."""
        )
        chain = LLMChain(llm=self.llm_instance, prompt=prompt)
        return chain.run(idea=query)
    
    async def _arun(self, query: str) -> str:
        raise NotImplementedError("Async not implemented")


class TrendInput(BaseModel):
    query: str = Field(description="The niche or industry to analyze trends for")


class TrendAnalysisTool(BaseTool):
    name = "trend_analyzer"
    description = "Analyzes current social media trends and provides insights. Use this when users want to know what's trending or how to align content with current trends."
    args_schema: Type[BaseModel] = TrendInput
    llm_instance: Any = None
    
    def __init__(self, llm):
        super().__init__()
        self.llm_instance = llm
        
    def _run(self, query: str) -> str:
        """Analyze trends in a niche"""
        prompt = PromptTemplate(
            input_variables=["niche"],
            template="""You are a social media trend analyst. Analyze the current trends in the following niche:

Niche: {niche}

Provide:
1. Top 5 trending topics/themes in this niche
2. Recommended content angles to leverage these trends
3. Best posting times and platforms for this niche
4. Emerging opportunities
5. Hashtag recommendations

Base your analysis on general social media best practices and current digital marketing trends."""
        )
        chain = LLMChain(llm=self.llm_instance, prompt=prompt)
        return chain.run(niche=query)
    
    async def _arun(self, query: str) -> str:
        raise NotImplementedError("Async not implemented")


class SchedulerInput(BaseModel):
    query: str = Field(description="The requirements for the posting schedule")


class PostSchedulerTool(BaseTool):
    name = "post_scheduler"
    description = "Creates a posting schedule and content calendar. Use this when users want to plan their content strategy or need a posting timeline."
    args_schema: Type[BaseModel] = SchedulerInput
    llm_instance: Any = None
    
    def __init__(self, llm):
        super().__init__()
        self.llm_instance = llm
        
    def _run(self, query: str) -> str:
        """Generate posting schedule"""
        prompt = PromptTemplate(
            input_variables=["requirements"],
            template="""You are a social media strategist. Create a content posting schedule based on these requirements:

Requirements: {requirements}

Provide:
1. A 7-day content calendar with specific post ideas for each day
2. Recommended posting times for each platform
3. Content mix strategy (educational, promotional, entertaining, etc.)
4. Engagement strategies for each post type
5. Key performance indicators to track

Format as a structured weekly plan."""
        )
        chain = LLMChain(llm=self.llm_instance, prompt=prompt)
        return chain.run(requirements=query)
    
    async def _arun(self, query: str) -> str:
        raise NotImplementedError("Async not implemented")
