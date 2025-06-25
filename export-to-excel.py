import pandas as pd
from datetime import datetime

# Data hasil revisi
data = [
    ["Kick-off & Analisis Kebutuhan", "Project Manager", "2025-07-01", "2025-07-12", 12],
    ["Desain UI/UX", "UI/UX Designer", "2025-07-01", "2025-07-21", 21],
    ["Sprint 1: Auth, Dashboard, Master Data", "Backend, Frontend, DevOps, QA", "2025-07-15", "2025-08-04", 21],
    ["Sprint 2: Registrasi & Data Pendaki", "Backend, Frontend, QA", "2025-07-29", "2025-08-18", 21],
    ["Sprint 3: Laporan, Sertifikat, Export", "Backend, Frontend, QA", "2025-08-12", "2025-09-01", 21],
    ["Integrasi & QA", "QA, DevOps, Backend, Frontend", "2025-08-26", "2025-09-06", 12],
    ["UAT & Revisi", "QA, Project Manager, Backend, Frontend", "2025-09-02", "2025-09-13", 12],
    ["Training & Go-Live", "Trainer, DevOps, Project Manager", "2025-09-09", "2025-09-20", 12],
    ["Garansi & Support", "All team (on demand)", "2025-09-16", "2025-12-22", 98]
]

# Buat DataFrame
columns = ["Task", "Team", "Start Date", "End Date", "Estimasi (Days)"]
df = pd.DataFrame(data, columns=columns)

# Simpan sebagai file Excel
df.to_excel("timeline-revisi-aplikasi-pendakian.xlsx", index=False, sheet_name="Gantt")
