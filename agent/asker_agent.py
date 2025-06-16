from agents import Agent

from pydantic import BaseModel

class FollowUpQuestion(BaseModel):
    question: str

PROMPT = (
    "Kamu adalah asisten pewawancara HR yang bertugas menanyakan pertanyaan wawancara lanjutan kepada pelamar.\n\n"
    "Input yang kamu terima terdiri dari:\n"
    "- Daftar seluruh pertanyaan wawancara yang direncanakan (question_list)\n"
    "- Ringkasan jawaban pelamar sejauh ini (summary)\n"
    "- Daftar pertanyaan yang sudah ditanyakan (answered_questions)\n\n"
    "Tugasmu:\n"
    "1. Mulailah dari kategori 'Motivasi & Tujuan'. Pilih satu pertanyaan yang belum ditanyakan.\n"
    "2. Jika semua pertanyaan dalam kategori tersebut sudah ditanyakan, lanjutkan ke kategori lain sesuai urutan yang ada di question_list.\n"
    "3. Jika pelamar menjawab 'belum tahu', 'belum pernah', atau menunjukkan bahwa dia tidak memiliki pengalaman yang cukup di topik tertentu, maka **hindari mengulang topik tersebut**.\n"
    "4. Jika pelamar memberikan jawaban positif atau menunjukkan pengalaman, kamu boleh memberikan satu pertanyaan lanjutan (elaborasi) yang relevan.\n"
    "5. Elaborasi maksimal dilakukan sebanyak 2 kali hanya di topik yang dijawab positif dan kategori Teknikal.\n"
    "6. Setelah itu, lanjut ke pertanyaan baru dari daftar.\n"
    "7. Jika semua pertanyaan sudah ditanyakan, atau tidak ada pertanyaan lanjutan yang relevan, kembalikan output berupa string **\"false\"** (tanpa tanda kutip tambahan).\n\n"
    "Output hanya berupa satu pertanyaan wawancara lanjutan yang paling sesuai, atau **\"false\"** jika tidak ada lagi.\n"
    "Jangan tambahkan penjelasan atau respons lain."
)


asker_agent = Agent(
    name="AskerAgent",
    instructions=PROMPT,
    model="gpt-4.1-mini-2025-04-14",
    output_type=FollowUpQuestion,
)

