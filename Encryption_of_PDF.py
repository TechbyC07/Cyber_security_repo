#ENCRYPTION OF PDF
import pikepdf

old_file = pikepdf.Pdf.open("sample.pdf")

no_extratcion = pikepdf.Permissions(extract= False)

old_file.save(
    "sample2.pdf",
    encryption=pikepdf.Encryption(
        user="hello",
        owner="subscribe",
        allow=no_extratcion
    )
)

print("PDF encrypted successfully!")