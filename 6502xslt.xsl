<?xml version="1.0" encoding="UTF-8"?>
    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
        xmlns:fo="http://www.w3.org/1999/XSL/Format" >
        <xsl:output method="text" omit-xml-declaration="yes" indent="yes"/>
        <xsl:strip-space elements="mnemonic"/>
        <xsl:template match="sixfivezerotwo">
      
            <xsl:value-of select="lines"/>
                
        </xsl:template>
        
    </xsl:stylesheet>
