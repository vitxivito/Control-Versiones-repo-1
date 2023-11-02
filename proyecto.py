from supabase import create_client, Client

supabase : Client = create_client("https://qpynwhslmdfavlxxpihu.supabase.co"), "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFweW53aHNsbWRmYXZseHhwaWh1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTYzMTk1NzEsImV4cCI6MjAxMTg5NTU3MX0.JKpztUNwvsJDuDpaYoUYOedFHqpkdOJVxNOaalY4KnM"
print(supabase.table ("Alumnos").select("*").eq("ID,"2,0)execute())
print("hola")
print("que tal")
