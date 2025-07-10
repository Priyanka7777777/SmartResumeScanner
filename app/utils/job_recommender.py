import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_jobs(user_skills, csv_path='data/job_descriptions.csv', top_n=5):
    # Load job data
    df = pd.read_csv(csv_path)

    # Combine user skills into a single string
    user_skills_str = " ".join(user_skills)

    # Combine with job descriptions
    job_corpus = df['description'].tolist() + [user_skills_str]

    # Vectorize
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(job_corpus)

    # Compute similarity (last row is user)
    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()

    # Get top matches
    top_indices = similarity_scores.argsort()[::-1][:top_n]
    recommendations = df.iloc[top_indices][['job_id', 'job_title', 'description']]
    recommendations['score'] = similarity_scores[top_indices]

    return recommendations.to_dict(orient='records')

