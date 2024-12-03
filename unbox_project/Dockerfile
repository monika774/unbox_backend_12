FROM python
WORKDIR /app
COPY requirements.txt .
# Install dependencies
# RUN pip install --no-cache-dir -r requirements.txt
# Copy the project into the container
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
