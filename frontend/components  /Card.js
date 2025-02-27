const Card = ({ title, children }) => {
    return (
      <div className="bg-white shadow-lg rounded-lg p-6">
        <h2 className="text-lg font-bold mb-3">{title}</h2>
        {children}
      </div>
    );
  };
  
  export default Card;  