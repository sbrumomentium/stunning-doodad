def pregunta_agua(mililitros: int) -> str:
    cajas20l = mililitros // 20000
    mililitros = mililitros % 20000

    bidon7l = mililitros // 7000
    mililitros = mililitros % 7000

    botella2l = mililitros // 2000
    mililitros = mililitros % 2000

    botella600ml = mililitros // 600
    mililitros = mililitros % 600
    return f"{cajas20l}:{bidon7l}:{botella2l}:{mililitros}"
