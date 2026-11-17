from fastapi import FastAPI


app = FastAPI(
    title="Task Manager API",
    description="API RESTful para gestão de tarefas. Fornece operações CRUD completas, validação rigorosa de dados e arquitetura escalável.",
    version="1.0.0"
)

@app.get("/")
async def root():
    return{"message":"Task Manager API operacional. Sistema pronto para receber requisições."}