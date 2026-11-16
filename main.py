from src.ensalamento import interface, executar

if __name__ == "__main__":
    import multiprocessing
    import shutil
    import sys
    from pathlib import Path

    from src.ui.recursos import diretorio_aplicacao

    multiprocessing.freeze_support()
    if len(sys.argv) > 1:
        try:
            entrada = Path(sys.argv[1]).expanduser().resolve()
            pasta_saida = diretorio_aplicacao() / "outputs" / "xlsx"
            pasta_saida.mkdir(parents=True, exist_ok=True)
            destino = pasta_saida / f"{entrada.stem}_ensalamento.xlsx"
            shutil.copy2(entrada, destino)
            print(executar(destino))
            print(f"Arquivo gerado: {destino}")
        except Exception as exc:
            print(f"Erro: {exc}", file=sys.stderr)
            raise SystemExit(1)
    else:
        interface()
