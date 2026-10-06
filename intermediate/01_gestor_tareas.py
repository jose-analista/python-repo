import json
from dataclasses import dataclass, asdict
from pathlib import Path


ARCHIVO = Path("tareas.json")


@dataclass
class Tarea:
    id: int
    titulo: str
    completada: bool = False


class GestorTareas:
    def __init__(self, archivo: Path):
        self.archivo = archivo
        self.tareas = self._cargar()

    def _cargar(self):
        if not self.archivo.exists():
            return []

        try:
            with self.archivo.open("r", encoding="utf-8") as archivo:
                datos = json.load(archivo)

            return [Tarea(**tarea) for tarea in datos]

        except (json.JSONDecodeError, TypeError, ValueError):
            print("Advertencia: el archivo de tareas no es válido.")
            return []

    def _guardar(self):
        with self.archivo.open("w", encoding="utf-8") as archivo:
            json.dump(
                [asdict(tarea) for tarea in self.tareas],
                archivo,
                indent=4,
                ensure_ascii=False
            )

    def agregar(self, titulo: str):
        if not titulo.strip():
            raise ValueError("El título no puede estar vacío.")

        nuevo_id = max(
            (tarea.id for tarea in self.tareas),
            default=0
        ) + 1

        tarea = Tarea(
            id=nuevo_id,
            titulo=titulo.strip()
        )

        self.tareas.append(tarea)
        self._guardar()

        print(f"Tarea #{nuevo_id} agregada correctamente.")

    def listar(self):
        if not self.tareas:
            print("No hay tareas registradas.")
            return

        for tarea in self.tareas:
            estado = "✓" if tarea.completada else "○"
            print(f"{estado} [{tarea.id}] {tarea.titulo}")

    def completar(self, tarea_id: int):
        for tarea in self.tareas:
            if tarea.id == tarea_id:
                tarea.completada = True
                self._guardar()
                print(f"Tarea #{tarea_id} completada.")
                return

        print("No se encontró la tarea.")

    def eliminar(self, tarea_id: int):
        tareas_originales = len(self.tareas)

        self.tareas = [
            tarea for tarea in self.tareas
            if tarea.id != tarea_id
        ]

        if len(self.tareas) == tareas_originales:
            print("No se encontró la tarea.")
            return

        self._guardar()
        print(f"Tarea #{tarea_id} eliminada.")


def mostrar_menu():
    print("\n=== GESTOR DE TAREAS ===")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")


def main():
    gestor = GestorTareas(ARCHIVO)

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ").strip()

        try:
            if opcion == "1":
                titulo = input("Título: ")
                gestor.agregar(titulo)

            elif opcion == "2":
                gestor.listar()

            elif opcion == "3":
                tarea_id = int(input("ID de la tarea: "))
                gestor.completar(tarea_id)

            elif opcion == "4":
                tarea_id = int(input("ID de la tarea: "))
                gestor.eliminar(tarea_id)

            elif opcion == "5":
                print("Programa finalizado.")
                break

            else:
                print("Opción no válida.")

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()