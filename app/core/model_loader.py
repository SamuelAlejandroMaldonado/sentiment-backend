from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM


sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)


gen_model_name = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(gen_model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(gen_model_name)

generator_model = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
    max_length=60
)
