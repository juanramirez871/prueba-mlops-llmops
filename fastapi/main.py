from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from transformers import pipeline
import funciones

app = FastAPI(
    title="API de Práctica FastAPI",
    description="Prueba keepcoding",
    version="1.0.0"
)


@app.get("/calcular-promedio")
def calcular_promedio(numeros: str, decimales: int = 2):
    try:
        lista_numeros = [float(n.strip()) for n in numeros.split(",")]
        resultado = funciones.calcular_promedio(lista_numeros, decimales)
        return {
            "numeros": lista_numeros,
            "promedio": resultado,
            "cantidad": len(lista_numeros)
        }
    except ValueError:
        raise HTTPException(status_code=400, detail="Formato de números inválido")

@app.get("/area-rectangulo")
def area_rectangulo(base: float, altura: float):
    if base <= 0 or altura <= 0:
        raise HTTPException(status_code=400, detail="Base y altura deben ser positivas")
    
    resultado = funciones.calcular_area_rectangulo(base, altura)
    return resultado


@app.get("/generar-texto")
def generar_texto(prompt: str, max_length: int = 50):
    try:
        text_generator = pipeline(
            "text-generation",
            model="distilgpt2"
        )
        
        resultado = text_generator(
            prompt,
            max_length=max_length,
            num_return_sequences=1,
            temperature=0.7
        )[0]
        
        return {
            "prompt_original": prompt,
            "texto_generado": resultado['generated_text'],
            "longitud_maxima": max_length,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en el pipeline: {str(e)}")

@app.get("/clasificar-texto")
def clasificar_texto(texto: str, categorias: str = "tecnología,deportes,política"):
    try:
        classifier = pipeline(
            "zero-shot-classification",
            model="facebook/bart-large-mnli"
        )
        
        lista_categorias = [cat.strip() for cat in categorias.split(",")]
        resultado = classifier(texto, lista_categorias)
        
        return {
            "texto": texto,
            "categoria_predicha": resultado['labels'][0],
            "confianza": round(resultado['scores'][0], 4),
            "todas_categorias": dict(zip(resultado['labels'], [round(s, 4) for s in resultado['scores']])),
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en el pipeline: {str(e)}")

@app.get("/estadisticas")
def estadisticas(valores: str, operacion: str = "estadisticas"):
    try:
        lista_valores = [float(v.strip()) for v in valores.split(",")]
        datos = {f"valor_{i+1}": v for i, v in enumerate(lista_valores)}
        
        resultado = funciones.procesar_datos(datos, operacion)
        resultado["valores_originales"] = lista_valores
        
        return resultado

    except ValueError:
        raise HTTPException(status_code=400, detail="Formato de valores inválido")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
