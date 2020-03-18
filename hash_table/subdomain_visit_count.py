def subdomainVisits(cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domain_dic = {}
        
        for d in cpdomains:
            count, domain = d.split()
            subdomains = domain.split(".")
            subdomains.reverse()
            
            subdomain = subdomains[0]
            domain_dic[subdomain] = domain_dic.get(subdomain, 0) + int(count)
            
            for s in subdomains[1:]:
                subdomain = s + "." + subdomain
                domain_dic[subdomain] = domain_dic.get(subdomain, 0) + int(count)
    
        domain_li = []
        for k, v in domain_dic.items():
            s = str(v) + " " + k
            domain_li.append(s)
        return domain_li

cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print(subdomainVisits(cpdomains))

