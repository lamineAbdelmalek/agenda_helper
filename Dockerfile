# Builder stage
FROM python:3.10-slim as builder

RUN pip install poetry==1.6.1

WORKDIR /linkedin_lookup

COPY pyproject.toml poetry.lock ./

RUN poetry export -f requirements.txt --without-hashes -o requirements.txt

# Final stage
FROM python:3.10-slim as final

WORKDIR /linkedin_lookup

COPY --from=builder /linkedin_lookup/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
RUN rm -f requirements.txt

COPY linkedin_lookup/ linkedin_lookup/
COPY pyproject.toml .

RUN pip install .

EXPOSE 8580

CMD sh -c "streamlit run linkedin_lookup/app.py --server.port=8580 --server.address=0.0.0.0"
