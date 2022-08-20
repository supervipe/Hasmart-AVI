FROM rasa/rasa:2.6.0-full

# Change back to root user to install dependencies
USER root

RUN python -m pip install --upgrade pip

RUN pip install https://github.com/explosion/spacy-models/releases/download/pt_core_news_lg-3.0.0/pt_core_news_lg-3.0.0-py3-none-any.whl

# Switch back to non-root to run code
USER 1001
