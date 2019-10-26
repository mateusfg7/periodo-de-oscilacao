def astro(parametros, astros):
    
    if parametros == 'sol':
        return astros['sol']
        
    elif parametros == 'mer':
        return astros['mercurio']
        
    elif parametros == 'ven':
        return astros['venus']
        
    elif parametros == 'ter':
        return astros['terra']
        
    elif parametros == 'mar':
        return astros['marte']
        
    elif parametros == 'jup':
        return astros['jupiter']
        
    elif parametros == 'sat':
        return astros['saturno']
        
    elif parametros == 'ura':
        return astros['urano']
        
    elif parametros == 'net':
        return astros['netuno']
        
    elif parametros == 'plu':
        return astros['plutao']
        
    elif parametros == 'lua':
        return astros['lua']
