from abc import ABC, abstractmethod
from typing import List


class Empleado(ABC):
    #Clase base para todos los empleados.
    #Todos los empleados tienen nombre y salario_base (se puede usar o no según el tipo).
    def __init__(self, nombre: str, salario_base: float = 0.0) -> None:
        self.nombre = nombre
        self.salario_base = float(salario_base)

    @abstractmethod
    def calcular_salario(self) -> float:
        #Metodo abstracto: cada subclase debe implementar su propio cálculo de salario
        pass

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(nombre={self.nombre})"


class EmpleadoTiempoCompleto(Empleado):
    #Empleado a tiempo completo: salario = salario_base + bono_fijo
    def __init__(self, nombre: str, salario_base: float, bono_fijo: float) -> None:
        super().__init__(nombre, salario_base)
        self.bono_fijo = float(bono_fijo)

    def calcular_salario(self) -> float:
        return self.salario_base + self.bono_fijo


class EmpleadoMedioTiempo(Empleado):
    #Empleado por horas / medio tiempo: salario = horas_trabajadas * tarifa_hora
    #(se mantiene salario_base por compatibilidad del modelo si fuera necesario)
    def __init__(self, nombre: str, horas_trabajadas: float, tarifa_hora: float, salario_base: float = 0.0) -> None:
        super().__init__(nombre, salario_base)
        self.horas_trabajadas = float(horas_trabajadas)
        self.tarifa_hora = float(tarifa_hora)

    def calcular_salario(self) -> float:
        return self.horas_trabajadas * self.tarifa_hora


def mostrar_salarios(empleados: List[Empleado]) -> None:
    #Recorre la lista de empleados y muestra el salario calculado usando polimorfismo.
    for e in empleados:
        try:
            salario = e.calcular_salario()
            print(f"{e.nombre} ({e.__class__.__name__}) -> Salario: ${salario:.2f}")
        except Exception as exc:
            print(f"Error calculando salario de {e.nombre}: {exc}")


if __name__ == "__main__":
    # Ejemplos de uso (prueba)
    emp1 = EmpleadoTiempoCompleto("Ana Pérez", salario_base=1500.0, bono_fijo=300.0)
    emp2 = EmpleadoMedioTiempo("Luis Gómez", horas_trabajadas=20, tarifa_hora=12.5)
    emp3 = EmpleadoTiempoCompleto("María López", salario_base=1800.0, bono_fijo=250.0)
    emp4 = EmpleadoMedioTiempo("Juan Torres", horas_trabajadas=15.5, tarifa_hora=10.0)

    empleados = [emp1, emp2, emp3, emp4]
    mostrar_salarios(empleados)