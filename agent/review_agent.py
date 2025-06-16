from pydantic import BaseModel

from agents import Agent

class Review(BaseModel):
    is_finish: bool

REVIEW_PROMPT = (
    "Kamu adalah reviewer HR yang bertugas mengevaluasi apakah sesi wawancara sudah cukup lengkap dan dapat dihentikan.\n\n"
    "Kamu akan diberikan:\n"
    "- Daftar seluruh pertanyaan wawancara yang direncanakan (terstruktur dalam kategori)\n"
    "- Daftar pertanyaan yang sudah dijawab pelamar\n"
    "- Ringkasan jawaban pelamar sejauh ini\n\n"
    "Tugasmu:\n"
    "1. Identifikasi apakah mayoritas kategori sudah memiliki minimal satu pertanyaan yang dijawab dengan baik.\n"
    "2. Evaluasi distribusi jawaban: Jika hanya satu kategori yang dominan atau sebagian besar kategori belum tersentuh, jawabannya belum cukup.\n"
    "3. Jika sebagian besar kategori sudah terwakili secara merata dan ringkasan mencerminkan pemahaman yang baik, maka wawancara boleh dihentikan.\n\n"
    "Outputkan hasil akhir dalam format JSON:\n"
    "{ \"is_finish\": true|false }\n"
)

review_agent = Agent(
    name="ReviewAgent",
    instructions=REVIEW_PROMPT,
    model="gpt-4.1-mini-2025-04-14",
    output_type=Review,
)