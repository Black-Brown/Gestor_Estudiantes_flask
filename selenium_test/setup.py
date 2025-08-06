#!/usr/bin/env python3
"""
Script para ejecutar las pruebas de Selenium y generar reportes
"""

import subprocess
import sys
import os
from datetime import datetime

def run_tests():
    """
    Ejecuta las pruebas de Selenium y genera reportes
    """
    print("🚀 Iniciando pruebas automatizadas con Selenium...")
    print("=" * 60)
    
    # Crear directorio para reportes si no existe
    if not os.path.exists("reports"):
        os.makedirs("reports")
    
    # Crear directorio para screenshots si no existe
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    
    # Generar timestamp para el reporte
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = f"reports/test_report_{timestamp}.html"
    
    # Comando para ejecutar las pruebas
    cmd = [
        "pytest",
        "test_auth.py",
        "test_students_crud.py",
        "-v",  # Verbose output
        "--html=" + report_file,  # Reporte HTML
        "--self-contained-html",  # HTML autónomo
        "--capture=no",  # Mostrar prints
        "--tb=short",  # Traceback corto
        "-x",  # Parar en el primer fallo
        "--maxfail=3"  # Máximo 3 fallos antes de parar
    ]
    
    try:
        print(f"📋 Ejecutando pruebas...")
        print(f"📊 Reporte se generará en: {report_file}")
        print(f"📸 Screenshots se guardarán en: screenshots/")
        print("-" * 60)
        
        # Ejecutar las pruebas
        result = subprocess.run(cmd, capture_output=False, text=True)
        
        print("-" * 60)
        
        if result.returncode == 0:
            print("✅ Todas las pruebas pasaron exitosamente!")
        else:
            print("❌ Algunas pruebas fallaron. Revisa el reporte para más detalles.")
        
        print(f"📊 Reporte HTML generado: {report_file}")
        print(f"📸 Screenshots disponibles en: screenshots/")
        
        return result.returncode
        
    except FileNotFoundError:
        print("❌ Error: pytest no está instalado. Ejecuta: pip install pytest pytest-html")
        return 1
    except Exception as e:
        print(f"❌ Error ejecutando las pruebas: {e}")
        return 1

def run_specific_test(test_file):
    """
    Ejecuta una prueba específica
    """
    print(f"🎯 Ejecutando prueba específica: {test_file}")
    
    cmd = [
        "pytest",
        test_file,
        "-v",
        "--capture=no",
        "--tb=short"
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=False, text=True)
        return result.returncode
    except Exception as e:
        print(f"❌ Error ejecutando la prueba: {e}")
        return 1

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Ejecutar prueba específica
        test_file = sys.argv[1]
        exit_code = run_specific_test(test_file)
    else:
        # Ejecutar todas las pruebas
        exit_code = run_tests()
    
    sys.exit(exit_code) 